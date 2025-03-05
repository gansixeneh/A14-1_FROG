import torch
import pandas as pd
from dotenv import load_dotenv

from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    MessagesPlaceholder,
)

from few_shots import (
    LEGAL_EXTRACT_ENTITY_FEW_SHOTS,
    LEGAL_GENERATE_SPARQL_FEW_SHOTS,
)

from pydantic import BaseModel, Field
from typing import List, Optional

from verbalization.legal import LegalVerbalization
from utils.helper import legal_entity_label
from property_retrieval.legal import LegalPropertyRetrieval
from .base import BaseGraphRAG

load_dotenv()

# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DEVICE = "cuda"


class LegalGraphRAG(BaseGraphRAG):
    def __init__(
        self,
        model_name: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        device: str = DEVICE,
        use_local_model: str = True,
        max_new_tokens: int = 1500,
        property_retrieval: Optional[LegalPropertyRetrieval] = None,
        generate_sparql_few_shot_messages: Optional[List[dict]] = None,
        always_use_generate_sparql: bool = False,
        use_local_weaviate_client: bool = True,
        print_output: bool = False,
        additional_model_kwargs: dict = {},
        turtle_file_path: str = "modified_data-lex2kg.ttl",
    ) -> None:
        super().__init__(
            model_name,
            device,
            use_local_model,
            max_new_tokens,
            always_use_generate_sparql,
            print_output,
            additional_model_kwargs,
            turtle_file_path,
        )
        self.verbalization = LegalVerbalization(
            turtle_file_path=turtle_file_path,
            model_name="jinaai/jina-embeddings-v3",
            query_model_encode_kwargs={
                "task": "retrieval.query",
                "prompt_name": "retrieval.query",
            },
            passage_model_encode_kwargs={
                "task": "retrieval.passage",
                "prompt_name": "retrieval.passage",
            },
        )
        if generate_sparql_few_shot_messages is None:
            self.generate_sparql_few_shot_messages = LEGAL_GENERATE_SPARQL_FEW_SHOTS
        else:
            self.generate_sparql_few_shot_messages = generate_sparql_few_shot_messages
        if property_retrieval is None:
            self.property_retrieval = LegalPropertyRetrieval(
                embedding_model_name="jinaai/jina-embeddings-v3",
                is_local_client=use_local_weaviate_client,
                turtle_file_path=turtle_file_path,
            )
        else:
            self.property_retrieval = property_retrieval

    def extract_entity(self, question, try_threshold=10):
        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )

        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=LEGAL_EXTRACT_ENTITY_FEW_SHOTS,
        )

        chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """- You are an entity extractor.
- Extract the entities from the given question! DO NOT hallucinate and only provide entities that are present in the question.
- These entities usage is to find the most appropriate entity to be used in SPARQL queries.
- If there is no entity in the question, return empty list.
- Sort the entities based on the importance of the entity in the question.
- ONLY return the entities. DO NOT return anything else.
- Make the entity singular, not plural. For instance, if the entity is foods, then transform it into food.
- DO NOT separate Proper Names, e.g. 'Amazon River' should be returned as 'Amazon River'.
- Even if there is only one entity, always return as a list.

Based on the query given, extract the entities from it and return the extracted entities in the format below.
{format_instructions}""",
                ),
                few_shot_prompt,
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        return super().extract_entity(question, chat_prompt_template, try_threshold)

    def get_most_appropriate_entity_uri(
        self,
        entity: str,
        question: str,
        retrieved_entities: list[dict],
        try_threshold: int = 10,
    ) -> str:
        class Resource(BaseModel):
            """
            Represents the most appropriate entity URI selected from a given list of retrieved entities.
            This URI is used in SPARQL queries to accurately answer the user's question.
            """

            uri: str = Field(
                ...,
                description="Entity URI",
            )

        chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """For the entity given, find the most appropriate entity uri from the list of retrieved entities given to be used in to generate SPARQL queries to answer the given question! ONLY return the entity uri from the list of retrieved resources given. DO NOT return anything else and DO NOT hallucinate. DO NOT include any explanations or apologies in your responses.
Based on the entity given, get the most appropriate entity uri from it and return the uri in the format below.
{format_instructions}""",
                ),
                MessagesPlaceholder("chat_history"),
                (
                    "human",
                    """Retrieved entities:
{retrieved_entities}

Question:
{question}

Entity: 
{input}

Entity URI:""",
                ),
            ]
        )

        resource = super().get_most_appropriate_entity_uri(
            entity,
            question,
            retrieved_entities,
            Resource,
            chat_prompt_template,
            try_threshold,
        )

        if resource is None:
            return None
        return resource.uri

    def generate_related_properties(
        self, question: str, try_threshold: int = 10
    ) -> list[str]:
        raise NotImplementedError(
            "This method is not implemented for the Enterprise Graph RAG."
        )

    def generate_sparql(
        self,
        question: str,
        entities: list[str],
        few_shots: list[dict[str, str]],
        use_cot: bool = True,
        verbose: bool = False,
        try_threshold: int = 10,
    ) -> tuple[str, list[dict[str, str]]]:
        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=few_shots,
        )

        chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """# INSTRUCTIONS
You are an assistant trained to generate SPARQL queries. Use the provided context to generate a valid SPARQL query. Based on the given entities and properties context, please generate a valid SPARQL query to answer the question! Return only the uri or literal only. Literals always have a type xsd:string, xsd:date, or xsd:integer. Do not use entities or properties outside of the context! Always generate following the format instruction.

# CONTEXT
- Ontology candidates: 
{ontology}

# FORMAT INSTRUCTIONS
{format_instructions}""",
                ),
                few_shot_prompt,
                MessagesPlaceholder("chat_history"),
                (
                    "human",
                    "{input}",
                ),
            ]
        )

        return super().generate_sparql(
            question,
            entities,
            chat_prompt_template,
            use_cot,
            verbose,
            try_threshold,
        )

    def process_context(
        self, question: str, context: list[dict[str, str]]
    ) -> tuple[str, list[dict[str, str]]]:
        if type(context) == list:
            if len(context) > 0:
                if list(context[0].values())[0].startswith("http://example.org/"):
                    labeled_entities = []
                    for c in context[:50]:
                        res_dct = []
                        for k, v in c:
                            if k.startswith("http://example.org/"):
                                k = legal_entity_label(k)
                            res_dct.append({k: str(v)})
                        labeled_entities.extend(res_dct)

                    context = labeled_entities

                context_str = f'The answer of "{question}" is '
                for c in context[:50]:
                    for k, v in c.items():
                        context_str += k + " = " + v + ", "
                context_str = context_str[:-2] + "."
            else:
                context_str = "I don't know"
        else:
            context_str = f'The answer of "{question}" is {context}'
        return context_str, context

    def run(
        self,
        question: str,
        use_cot: bool = True,
        use_transform_factoid: bool = False,
        output_uri: bool = False,
        verbose: int = 0,
        try_threshold: int = 10,
    ):
        return super().run(
            question,
            use_cot=use_cot,
            output_uri=output_uri,
            use_transform_factoid=use_transform_factoid,
            verbose=verbose,
            try_threshold=try_threshold,
        )

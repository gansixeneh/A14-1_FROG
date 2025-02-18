from utils.helper import legal_entity_label, legal_property_label
from utils.api import DBPediaAPI
from verbalization.base import BaseVerbalization
import pandas as pd


class LegalVerbalization(BaseVerbalization):
    # modify depending on the enterprise ontology
    SENTENCE_TEMPLATE = "{p} dari {s} adalah {o}"
    SENTENCE_TEMPLATE_BAGIAN_DARI = "{s} merupakan {p} {o}"
    PO_TEMPLATE = """
SELECT DISTINCT
    ?p ?o
WHERE {{
    <{entity}> ?p ?o. 
    FILTER(STRSTARTS(STR(?p), STR(lex2kg-o:)))
}}
"""
    SP_TEMPLATE = """
SELECT DISTINCT
    ?s ?p
WHERE {{ 
        ?s ?p <{entity}>.
        FILTER(STRSTARTS(STR(?p), STR(lex2kg-o:)))
}}
"""

    def __init__(
        self,
        turtle_file_path: str,
        model_name="jinaai/jina-embeddings-v3",
        model_kwargs={"trust_remote_code": True},
        query_model_encode_kwargs={},
        passage_model_encode_kwargs={},
    ) -> None:
        super().__init__(
            model_name,
            model_kwargs,
            query_model_encode_kwargs,
            passage_model_encode_kwargs,
            turtle_file_path=turtle_file_path,
        )

    def get_po(self, entity: str) -> pd.DataFrame:
        query = self.PO_TEMPLATE.format(entity=entity)
        response = self.graph.query(query)
        df = pd.DataFrame(response.bindings)
        if not df.empty:
            df.columns = [str(col) for col in df.columns]
            
            df["sLabel"] = legal_entity_label(entity)
            df["pLabel"] = df["p"].apply(legal_property_label)
            df["oLabel"] = df["o"].apply(legal_entity_label)
            
            cols = ["s", "p", "sLabel", "pLabel", "oLabel"]
            df = df[cols]
            
            for col in cols:
                df[col] = df[col].apply(lambda x: str(x))
        if df.empty:
            return pd.DataFrame(columns=["p", "o", "sLabel", "pLabel", "oLabel"])
        return df

    def get_sp(self, entity: str) -> pd.DataFrame:
        query = self.SP_TEMPLATE.format(entity=entity)
        response = self.graph.query(query)
        df = pd.DataFrame(response.bindings)
        if not df.empty:
            df.columns = [str(col) for col in df.columns]
            
            df["sLabel"] = df["s"].apply(legal_entity_label)
            df["pLabel"] = df["p"].apply(legal_property_label)
            df["oLabel"] = legal_entity_label(entity)
            
            cols = ["s", "p", "sLabel", "pLabel", "oLabel"]
            df = df[cols]
            
            for col in cols:
                df[col] = df[col].apply(lambda x: str(x))
        if df.empty:
            return pd.DataFrame(columns=["s", "p", "sLabel", "pLabel", "oLabel"])
        return df

if __name__ == "__main__":
    legal_verbalization = LegalVerbalization(
        turtle_file_path="data/legal_turtle/data-lex2kg.ttl",
        model_name="jinaai/jina-embeddings-v3",
        model_kwargs={"trust_remote_code": True},
        query_model_encode_kwargs={
            "task": "retrieval.query",
            "prompt_name": "retrieval.query",
        },
        passage_model_encode_kwargs={
            "task": "retrieval.passage",
            "prompt_name": "retrieval.passage",
        },
    )

    legal_verbalization.get_sp("https://example.org/lex2kg/uu/1997/20/pasal/0023/versi/19970523")
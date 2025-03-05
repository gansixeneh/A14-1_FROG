import pandas as pd
from rdflib import Graph

from utils.helper import legal_entity_label, legal_property_label
from property_retrieval.base import BasePropertyRetrieval


class LegalPropertyRetrieval(BasePropertyRetrieval):
    def __init__(
        self,
        embedding_model_name: str = "jinaai/jina-embeddings-v3",
        is_local_client: bool = False,
        turtle_file_path: str = "data/legal_turtle/data-lex2kg.ttl",
    ) -> None:
        get_entities_query = """
SELECT DISTINCT
    (REPLACE(STR(?entity), "https://example.org/lex2kg/", "lex2kg/") AS ?short)
WHERE {
  { 
    ?entity ?predicate ?object. 
    FILTER(isIRI(?entity) && STRSTARTS(STR(?entity), "https://example.org/lex2kg/") && STRSTARTS(STR(?predicate), STR(lex2kg-o:)))
  }
  UNION
  { 
    ?subject ?predicate ?entity. 
    FILTER(isIRI(?entity) && STRSTARTS(STR(?entity), "https://example.org/lex2kg/") && STRSTARTS(STR(?predicate), STR(lex2kg-o:)))
  }
}
"""

        get_properties_query = """
SELECT DISTINCT
    (REPLACE(STR(?property), "https://example.org/lex2kg/ontology/", "lex2kg-o:") AS ?short)
WHERE {
  ?subject ?property ?object.
  FILTER(STRSTARTS(STR(?property), STR(lex2kg-o:)))
}
"""
        
        super().__init__(
            db_collection_name="modified_legal_property_db",
            embedding_model_name=embedding_model_name,
            is_local_client=is_local_client,
        )
        
        if self.is_collection_empty:
            g = Graph().parse(turtle_file_path)
            entity_response = g.query(get_entities_query)
            property_response = g.query(get_properties_query)
            df_entities = pd.DataFrame(entity_response.bindings)
            df_properties = pd.DataFrame(property_response.bindings)
            df_entities.columns = [str(col) for col in df_entities.columns]
            df_properties.columns = [str(col) for col in df_properties.columns]
            
            for col in df_entities.columns:
                df_entities[col] = df_entities[col].apply(lambda x: str(x))
            
            df_entities["label"] = df_entities["short"].apply(legal_entity_label)
            df_properties["label"] = df_properties["short"].apply(legal_property_label)

            df_entities.to_csv("entities.csv")
            df_properties.to_csv("properties.csv")
            emb_entities = self.model_embed.encode(
                df_entities["label"].tolist(), show_progress_bar=True
            )
            emb_properties = self.model_embed.encode(
                df_properties["label"].tolist(), show_progress_bar=True
            )
            legal_df_vectors = {
                "entities": (df_entities, emb_entities),
                "properties": (df_properties, emb_properties),
            }
            
            with self.collection.batch.fixed_size(batch_size=20) as batch:
                for key, (df, vector) in legal_df_vectors.items():
                    for i, row in df.iterrows():
                        batch.add_object(
                            properties={**row.to_dict(), "type": key},
                            vector=vector[i].tolist(),
                        )

    def search_entities(self, q: str, k: int = 5) -> pd.DataFrame:
        return self._search(q, type="entities", k=k)

    def search_properties(self, q: str, k: int = 5) -> pd.DataFrame:
        return self._search(q, type="properties", k=k)

    def get_related_candidates(
        self,
        q: str,
        property_candidates: list[str] = [],
        threshold: int = 0.5,
        k: int = 5,
    ) -> dict[str, list[str]]:
        tokens = self._preprocess_into_tokens(q)
        ngrams = self._generate_ngrams(tokens)
        result = {"entities": [], "properties": []}

        def search(ngram, type, threshold=threshold):
            df_res = self._search(ngram, type=type, k=k)
            result = (
                df_res[df_res["score"] >= threshold]["short"]
                .tolist()
            )
            return type, result

        for ngram in ngrams + property_candidates:
            for type in result.keys():
                type, df_res = search(ngram, type)
                if df_res:
                    result[type].extend(df_res)
                    result[type] = list(set(result[type]))

        return result

if __name__ == '__main__':
    property_retrieval = LegalPropertyRetrieval(
        embedding_model_name="jinaai/jina-embeddings-v3",
        is_local_client=False,
        turtle_file_path='data/legal_turtle/modified_data-lex2kg.ttl',
    )
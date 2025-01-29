import pandas as pd
import weaviate.classes as wvc

from property_retrieval.base import BasePropertyRetrieval


class DBPediaPropertyRetrieval(BasePropertyRetrieval):
    def __init__(
        self,
        df_classes: pd.DataFrame,
        df_oproperties: pd.DataFrame,
        df_dproperties: pd.DataFrame,
        embedding_model_name: str = "jinaai/jina-embeddings-v3",
        is_local_client: bool = True,
    ) -> None:
        super().__init__(
            db_collection_name="dbpedia_property_db",
            embedding_model_name=embedding_model_name,
            is_local_client=is_local_client,
        )
        self.df_classes = df_classes
        self.df_oproperties = df_oproperties
        self.df_dproperties = df_dproperties

        if self.is_collection_empty:
            emb_classes = self.model_embed.encode(
                self.df_classes["label"].tolist(), show_progress_bar=True
            )
            emb_oproperties = self.model_embed.encode(
                self.df_oproperties["label"].tolist(), show_progress_bar=True
            )
            emb_dproperties = self.model_embed.encode(
                self.df_dproperties["label"].tolist(), show_progress_bar=True
            )
            dbpedia_df_vectors = {
                "classes": (self.df_classes, emb_classes),
                "objProperties": (self.df_dproperties, emb_dproperties),
                "dataProperties": (self.df_oproperties, emb_oproperties),
            }
            with self.collection.batch.dynamic() as batch:
                for key, (df, vector) in dbpedia_df_vectors.items():
                    for i, row in df.iterrows():
                        batch.add_object(
                            properties={**row.to_dict(), "type": key},
                            vector=vector[i].tolist(),
                        )

    def search_classes(self, q: str, k: int = 5) -> pd.DataFrame:
        return self._search(q, type="classes", k=k)

    def search_oproperties(self, q: str, k: int = 5) -> pd.DataFrame:
        return self._search(q, type="objProperties", k=k)

    def search_dproperties(self, q: str, k: int = 5) -> pd.DataFrame:
        return self._search(q, type="dataProperties", k=k)

    def get_related_candidates(
        self,
        q: str,
        property_candidates: list[str] = [],
        threshold: int = 0.5,
        k: int = 5,
    ) -> dict[str, list[str]]:
        tokens = self._preprocess_into_tokens(q)
        ngrams = self._generate_ngrams(tokens)
        result = {"classes": [], "objProperties": [], "dataProperties": []}

        def search(ngram, type, threshold=threshold):
            def format_result(x):
                if type == "objProperties" or type == "dataProperties":
                    record = df_res[df_res["short"] == x][["shortDomain", "shortRange"]]
                    record.rename(
                        columns={
                            "shortDomain": "domain",
                            "shortRange": "range",
                        },
                        inplace=True,
                    )
                    record = record.to_dict(orient="records")[0]
                    if record["domain"] is None or record["domain"] == 'NaN':
                        del record["domain"]
                    if record["range"] is None or record["range"] == 'NaN':
                        del record["range"]
                    if record:
                        return f"{x}: {record}"
                    return "{x}: No domain and range"
                return x

            df_res = self._search(ngram, type=type, k=k)
            result = (
                df_res[df_res["score"] >= threshold]["short"]
                .apply(format_result)
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

from langchain.vectorstores import Chroma
from langchain_core.documents.base import Document
from langchain_core.embeddings.embeddings import Embeddings

from yandex_cloud_ml_sdk import YCloudML

def validate_skill(skill_source:str):
    return NotImplementedError

class YandexEmbeddingModel(Embeddings):
    def __init__(self):
        super.__init__()
        self.sdk = YCloudML(
        folder_id="<идентификатор_каталога>",
        auth="<API-ключ>")
        self.doc_model = self.sdk.models.text_embeddings("doc")
        self.query_model = self.sdk.models.text_embeddings("query")
    
    def embed_documents(self, texts):
        return [self.doc_model.run(t) for t in texts]
    
    def embed_query(self, text):
        return self.query_model(text)

def add_skill_db(db, skill_description:str, skill_source:str):
    doc = Document(page_content = skill_description, metadata = {"code": skill_source})
    db.add_documents([doc])

def fetch_skill_db(vectordb, target_task:str):
    docs = [text.metadata["code"] for text, sim in 
            vectordb.similarity_search_with_relevance_scores(target_task, 5, score_threshold = 0.5)]
    return docs

def init_db(db_src:str):
    emb_model = YandexEmbeddingModel()
    vectordb = Chroma(persist_directory=db_src, embedding_function=emb_model)
    vectordb.persist()
    return vectordb
from langchain.vectorstores import Chroma
from langchain_core.documents.base import Document
from yandex_cloud_ml_sdk import YCloudML

def validate_skill(skill_source:str):
    return "hello"

class YandexEmbeddingModel:
    def __init__(self, sdk):
        self.doc_model = sdk.models.text_embeddings("doc")
        self.query_model = sdk.models.text_embeddings("query")
    
    def embed_documents(self, texts):
        return [self.doc_model.run(t) for t in texts]
    
    def embed_query(self, text):
        return self.query_model.run(text)

class SkillManager:
    def __init__(self, db_src: str, sdk, system_prompt_src):
        emb_model = YandexEmbeddingModel(sdk)
        with open(system_prompt_src) as f:
            system_prompt(f.read())
        self.db = Chroma(persist_directory=db_src, embedding_function=emb_model)
        self.db.persist()

    def fetch_skills(self, target_task:str):
        docs = [text.metadata["code"] for text, sim in \
                self.db.similarity_search_with_relevance_scores(target_task, 5, score_threshold = 0.5)]
        return docs
    
    def get_description(self, skill_source:str):
        descr = model(skill_source)
        return descr

    def add_skill(self, skill_source:str):
        skill_description = self.get_description(skill_source)
        doc = Document(page_content = skill_description, metadata = {"code": skill_source})
        self.db.add_documents([doc])
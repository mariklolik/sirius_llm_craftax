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
    def __init__(self, db_src: str, sdk):
        emb_model = YandexEmbeddingModel(sdk)
        self.gpt = sdk.models.completions("yandexgpt")
        self.gpt = self.gpt.configure(temperature=0.0)
        with open("SkillDescriptorSystemPrompt.txt") as f:
            self.system_prompt = f.read()
        self.db = Chroma(persist_directory=db_src, embedding_function=emb_model)

        files_with_functions = ["simple_actions.py", "checks.py", "explore.py", "explore_until.py", "utils.py", "move_to_node_smart.py", "mine_block.py"]
        for file_name in files_with_functions:
            with open("/../primitives/" + file_name) as f:
                text = f.read()
                funcs = self.split_functions(text)
                for func in funcs:
                    self.add_skill(func)

    def split_functions(code: str):
        lines = code.split('\n')
        res = []
        i = 0
        while i < len(lines):
            if lines[i][:min(3, len(lines[i]))] == "def":
                func = lines[i] + '\n'
                while(i < len(lines)):
                    if (lines[i][:min(4, len(lines[i]))] == " " * 4):
                        func += lines[i] + '\n'
                    else:
                        break 
                    i += 1
                res.append(func)
        return res


    def fetch_skills(self, target_task:str):
        docs = [(text.page_content, text.metadata["code"]) for text, sim in \
                self.db.similarity_search_with_relevance_scores(target_task, 5, score_threshold = 0.5)]
        return docs
    
    def get_description(self, skill_source:str):
        descr = self.gpt.run([
            {"role": "system",
             "text": self.system_prompt},
            {"role": "user",
             "text": skill_source}
        ]).alternatives[0].text
        return descr

    def add_skill(self, skill_source:str):
        skill_description = self.get_description(skill_source)
        doc = Document(page_content = skill_description, metadata = {"code": skill_source})
        self.db.add_documents([doc])

    def save(self):
        self.db.persist()
from langchain.vectorstores import Chroma
from langchain_core.documents.base import Document
import logging

logger = logging.getLogger("SkillManager")


class YandexEmbeddingModel:
    def __init__(self, sdk):
        self.doc_model = sdk.models.text_embeddings("doc")
        self.query_model = sdk.models.text_embeddings("query")

    def embed_documents(self, texts):
        return [list(self.doc_model.run(t)) for t in texts]

    def embed_query(self, text):
        return list(self.query_model.run(text))


class SkillManager:
    def __init__(self, db_src: str, sdk):
        emb_model = YandexEmbeddingModel(sdk)
        self.gpt = sdk.models.completions("yandexgpt")
        self.gpt = self.gpt.configure(temperature=0.0)
        with open("system_promts/skill_manager.txt", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.db = Chroma(
            persist_directory=db_src, embedding_function=emb_model
        )
        if len(self.db) == 0:
            files_with_functions = [
                "simple_actions.py",
                "checks.py",
                "explore.py",
                "explore_until.py",
                "utils.py",
                "move_to_node_smart.py",
                "mine_block.py",
            ]
            logger.info("Primitives spliting started")
            for file_name in files_with_functions:
                with open("primitives/" + file_name, encoding="utf-8") as f:
                    text = f.read()
                    funcs = self.split_functions(text)
                    for func in funcs:
                        self.add_skill(func)
            logger.info("Primitives spliting finished")
                    

    @staticmethod
    def split_functions(code: str):
        lines = code.split('\n')
        res = []
        i = 0
        while i < len(lines):
            if lines[i][:min(3, len(lines[i]))] == "def":
                func = lines[i] + '\n'
                while(True):
                    i += 1
                    if i == len(lines):
                        break
                    if lines[i][:min(4, len(lines[i]))] == " " * 4\
                        or (len(lines[i]) and lines[i][0] == ')')\
                        or len(lines[i]) == 0:
                        func += lines[i] + '\n'
                    else:
                        break 
                res.append(func)
            else:
                i += 1
        return res


    def fetch_skills(self, target_task: str):
        docs = [
            (text.page_content, text.metadata["code"])
            for text in self.db.similarity_search(
                target_task, k=7
            )
        ]
        return docs

    def get_description(self, skill_source: str):
        descr = (
            self.gpt.run(
                [
                    {"role": "system", "text": self.system_prompt},
                    {"role": "user", "text": skill_source},
                ]
            )
            .alternatives[0]
            .text
        )
        return descr

    def add_skill(self, skill_source: str):
        skill_description = self.get_description(skill_source)
        doc = Document(
            page_content=skill_description, metadata={"code": skill_source}
        )
        self.db.add_documents([doc])
        logger.info(f'Skill added {skill_description}')

    def save(self):
        self.db.persist()

# store.py
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

class VectorStore:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.store = None

    def create_store(self, texts: list[str]):
        docs = [Document(page_content=t) for t in texts]
        self.store = FAISS.from_documents(docs, self.embedding_model)

    def add_texts(self, texts: list[str]):
        docs = [Document(page_content=t) for t in texts]
        self.store.add_documents(docs)

    def similarity_search(self, query: str, k: int = 5):
        return self.store.similarity_search(query, k=k)
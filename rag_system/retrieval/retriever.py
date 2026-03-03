# retriever.py
from rag_system.vectorstore.store import VectorStore

class RAGRetriever:
    def __init__(self, vectorstore: VectorStore):
        self.vectorstore = vectorstore

    def retrieve(self, query: str, top_k: int = 5):
        results = self.vectorstore.similarity_search(query, k=top_k)
        return [doc.page_content for doc in results]
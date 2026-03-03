from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from utils.config import HF_API_TOKEN

def create_rag_chain(retriever, model_name="google/flan-t5-small"):
    """Return a RetrievalQA chain using Hugging Face Hub LLM"""
    llm = HuggingFaceHub(
        repo_id=model_name,
        model_kwargs={"temperature": 0.1, "max_length": 512},
        huggingfacehub_api_token=HF_API_TOKEN
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever.vectorstore.store.as_retriever(),
        chain_type="stuff"
    )
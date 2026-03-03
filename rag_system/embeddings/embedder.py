from langchain.embeddings import HuggingFaceEmbeddings
from utils.config import HF_API_TOKEN

def get_embedding_model():
    """Return Hugging Face embeddings model"""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=HF_API_TOKEN
    )
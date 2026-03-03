# app.py
import gradio as gr
from rag_system.ingestion.loader import load_pdf
from rag_system.ingestion.splitter import split_text
from rag_system.embeddings.embedder import get_embedding_model
from rag_system.vectorstore.store import VectorStore
from rag_system.retrieval.retriever import RAGRetriever
from rag_system.rag_chain.chain import create_rag_chain

# Initialize embeddings and vectorstore
embedding_model = get_embedding_model()
vectorstore = VectorStore(embedding_model)

def process_file(file):
    text = load_pdf(file.name)
    chunks = split_text(text)
    vectorstore.create_store(chunks)
    return "File processed successfully!"

def answer_question(query):
    retriever = RAGRetriever(vectorstore)
    qa_chain = create_rag_chain(retriever)
    return qa_chain.run(query)

with gr.Blocks() as demo:
    gr.Markdown("# RAG System")
    with gr.Tab("Upload File"):
        file_input = gr.File(label="Upload PDF")
        upload_btn = gr.Button("Process File")
        upload_btn.click(process_file, inputs=file_input, outputs=None)

    with gr.Tab("Ask Question"):
        query_input = gr.Textbox(label="Ask something")
        answer_output = gr.Textbox(label="Answer")
        ask_btn = gr.Button("Get Answer")
        ask_btn.click(answer_question, inputs=query_input, outputs=answer_output)

demo.launch()
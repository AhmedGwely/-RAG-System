# 📚 RAG System – Modular Document QA

This repository contains a fully modular **Retrieval-Augmented Generation (RAG)** system built using **LangChain**.  
The system allows users to upload a **PDF document**, index its contents into a vector database, and ask questions whose answers come directly from the PDF.

---

## 🚀 Project Objectives

- Build a complete RAG pipeline (Document Loading → Chunking → Embedding → VectorStore → Retrieval → Answering).
- Keep the entire project **modular** (no notebooks).
- Use **LangChain** for all RAG components.
- Allow students to choose any **Vector DB** and **LLM**, with justification in a 1-page summary.
- Include a simple **frontend** (recommended: Gradio).
- Include a `/test_data` folder with the sample PDF used for evaluation.

---

## 🧱 Repository Structure

# Project Repository Structure

```
rag-system/
│
├── src/
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   └── __init__.py
│   │
│   ├── embeddings/
│   │   ├── embedder.py
│   │   └── __init__.py
│   │
│   ├── vectorstore/
│   │   ├── store.py
│   │   └── __init__.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── __init__.py
│   │
│   ├── llm/
│   │   ├── llm_chain.py
│   │   └── __init__.py
│    
│  ├── app/
│  │  ├── frontend.py # Gradio / Streamlit
│  │  └── __init__.py
│  
├── config.py
├── test_data/
│    └─ sample.pdf
├─ 1_page_summary.pdf
├─ requirements.txt
├─ README.md
└─ main.py
```

## ⚙️ Installation

### 1. Clone the repo
```
- git clone <repo-url>
- cd rag-system
```


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
rag_project/
│
├── README.md
├── requirements.txt          # كل الباكيجات المطلوبة (langchain, gradio, VDB, LLM SDKs ...)
├── setup.py                  # لو هنعمل installable package
│
├── test_data/                # PDFs للتجربة
│   └── sample.pdf
│
├── rag_system/               # كل الكود الأساسي هنا
│   ├── __init__.py
│   ├── ingestion/            # لتحميل وفصل البيانات
│   │   ├── loader.py         # قراءة PDF / txt
│   │   └── splitter.py       # فصل النصوص لchunks
│   │
│   ├── embeddings/           # إنشاء الـembeddings
│   │   ├── embedder.py       # wrapper للembedding model
│   │   └── __init__.py
│   │
│   ├── vectorstore/          # الـVector DB
│   │   ├── store.py          # CRUD operations مع الـVDB
│   │   └── __init__.py
│   │
│   ├── retrieval/            # RAG retriever
│   │   ├── retriever.py      # retrieval logic
│   │   └── __init__.py
│   │
│   └── rag_chain/            # Chain + LLM
│       ├── chain.py          # RAG pipeline logic
│       └── __init__.py
│
├── frontend/                 # Gradio / أي واجهة
│   ├── app.py
│   └── __init__.py
│
└── utils/                    # أي أدوات مساعدة
    ├── config.py             # إعدادات LLM / VDB
    └── helpers.py
```

## ⚙️ Installation

### 1. Clone the repo
```
- git clone <repo-url>
- cd rag-system
```


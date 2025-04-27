# Retrieval-Augmented Generation (RAG) Chatbot Demo

This is a simplified demo for a RAG-based document assistant system. It:

- Loads multiple document types (PDF, Word, CSV, Text)
- Chunks and embeds them using state-of-the-art models
- Stores them in a local FAISS vector index
- Offers an API (`/ask`) using FastAPI to retrieve relevant chunks

## How to Run

1. Install dependencies:

```bash
pip install langchain sentence-transformers faiss-cpu fastapi uvicorn python-docx pandas
```

2. Prepare your documents:
Place your files in the `documents/` folder (you can use `.pdf`, `.docx`, `.csv`, `.txt`).

3. Run the demo script to build the vector index:

```bash
python rag_demo.py
```

4. Start the API server:

```bash
uvicorn rag_api:app --reload
```

5. Visit `http://127.0.0.1:8000/docs` to test your queries!

---

## Why This Matters

This is just the foundation. The full system includes:

- Advanced retrieval tuning (HyDE, self-ask, rerank)
- OpenAI/GPT integration for high-quality responses
- Caching, rate limits, GPU support
- Citation-based answers and dashboards for QA
- Scalable deployment for enterprise

## Note

This demo is a **lightweight example** to demonstrate capability and rapid prototyping.  
We can scale this into a **production-ready RAG system** within 4–6 weeks, including:

- Full support for internal + customer support docs
- Hybrid search (vector + keyword)
- High-accuracy, low-latency chatbot on your site
- Admin dashboard, quality metrics, and LLM cost controls

---

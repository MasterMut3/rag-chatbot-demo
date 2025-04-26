# === RAG FastAPI Server ===
# Simple API to query your document collection.

from fastapi import FastAPI
from pydantic import BaseModel
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

app = FastAPI()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index_multifile", embedding_model)
retriever = db.as_retriever()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_question(req: QueryRequest):
    relevant_docs = retriever.get_relevant_documents(req.query)
    results = [{"content": doc.page_content} for doc in relevant_docs[:3]]
    return {"results": results}

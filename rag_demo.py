# === Multi-Format RAG Demo ===
# Load PDFs, Word, CSV files, embed them and save FAISS index.

import os
from langchain.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, CSVLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(file_path)
        elif filename.endswith(".csv"):
            loader = CSVLoader(file_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            print(f"Unsupported file: {filename}")
            continue
        docs = loader.load()
        documents.extend(docs)
    return documents

folder_path = "documents"
documents = load_documents(folder_path)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding_model)
db.save_local("faiss_index_multifile")
print("Embeddings saved.")

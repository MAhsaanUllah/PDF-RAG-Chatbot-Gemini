import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain.docstore.document import Document
import pickle

# Set your API key (or load from environment)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCKYy-ijqx88F3LbrK39HMPZL8PR9Y3-74"  # replace this securely!

from phase1_load_pdf import load_pdf, clean_text, split_text

def make_documents(chunks):
    """Convert chunks to LangChain Document format"""
    return [Document(page_content=chunk) for chunk in chunks]

def embed_and_store(docs, save_path="faiss_index"):
    """Embed documents and store in FAISS"""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.from_documents(docs, embedding=embeddings)
    db.save_local(save_path)
    print(f"✅ FAISS DB saved to {save_path}")

if __name__ == "__main__":
    print("📄 Loading and splitting PDF...")
    text = load_pdf("sample.pdf")
    cleaned = clean_text(text)
    chunks = split_text(cleaned)

    print("📦 Creating documents...")
    docs = make_documents(chunks)

    print("🔍 Embedding and storing in FAISS...")
    embed_and_store(docs)

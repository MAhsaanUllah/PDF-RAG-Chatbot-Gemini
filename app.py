import streamlit as st
import os

# ---- Load API Key ----
api_key = st.secrets.get("GOOGLE_API_KEY", None)
if not api_key:
    st.error("🚨 GOOGLE_API_KEY missing in Streamlit Secrets. Add it in the Secrets panel.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

# ---- Imports (compatible versions only) ----
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

# ---- UI ----
st.set_page_config(page_title="Gemini RAG Chatbot", layout="wide")
st.title("📚 Gemini PDF Chatbot")

uploaded_files = st.sidebar.file_uploader(
    "📄 Upload PDF files", type="pdf", accept_multiple_files=True
)

if "qa" not in st.session_state:
    st.session_state.qa = None

if "history" not in st.session_state:
    st.session_state.history = []


# ---- Process PDFs ----
if uploaded_files:
    all_docs = []

    for file in uploaded_files:
        temp_path = f"temp_{file.name}"
        with open(temp_path, "wb") as f:
            f.write(file.read())

        loader = PyPDFLoader(temp_path)
        pdf_docs = loader.load()
        all_docs.extend(pdf_docs)

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(all_docs)

    embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = FAISS.from_documents(docs, embed)

    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    st.session_state.qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True
    )

# ---- Chat ----
if st.session_state.qa:
    st.subheader("💬 Chat with your PDFs")

    prompt = st.chat_input("Ask something...")

    if prompt:
        result = st.session_state.qa.invoke({"query": prompt})

        st.session_state.history.append(("user", prompt))
        st.session_state.history.append(("bot", result["result"]))

    for role, msg in st.session_state.history:
        with st.chat_message(role):
            st.write(msg)


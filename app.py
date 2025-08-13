import streamlit as st
import os
import asyncio
from dotenv import load_dotenv

# 🩹 Fix: Ensure there's an asyncio event loop (for Gemini async client)
try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("🚨 GOOGLE_API_KEY not found in .env file. Please add it to your .env and restart the app.")
    st.stop()
os.environ["GOOGLE_API_KEY"] = api_key  # For langchain_google_genai to pick up

# ---- LangChain & Gemini Modules ----
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# ---- Streamlit Config ----
st.set_page_config(page_title="Gemini RAG Chatbot", layout="wide")
st.title("📚 Gemini RAG Chatbot")
st.markdown("Upload one or more PDFs and ask questions using Google's Gemini LLM.")

# ---- Sidebar Upload ----
uploaded_files = st.sidebar.file_uploader("📄 Upload PDF files", type="pdf", accept_multiple_files=True)

# ---- Session State Initialization ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# ---- Process PDFs and Setup QA Chain ----
if uploaded_files:
    all_docs = []

    for file in uploaded_files:
        file_path = f"temp_{file.name}"
        with open(file_path, "wb") as f:
            f.write(file.read())

        loader = PyMuPDFLoader(file_path)
        documents = loader.load()
        all_docs.extend(documents)

    # Text Splitting & Vector Index
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(all_docs)

    # ✅ Correct Embedding Model (Gemini-compatible)
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = FAISS.from_documents(docs, embedding)

    # ✅ Correct LLM model
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")

    # Build QA chain
    st.session_state.qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True
    )

# ---- Chat Interface ----
if st.session_state.qa_chain:
    st.subheader("💬 Chat with your PDFs")
    user_input = st.chat_input("Ask something about the uploaded PDFs...")

    if user_input:
        with st.spinner("Gemini is thinking..."):
            result = st.session_state.qa_chain.invoke({"query": user_input})

        # Save chat history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", result["result"]))

    # Display chat history in order
    for role, msg in st.session_state.chat_history:
        with st.chat_message("user" if role == "user" else "assistant"):
            st.markdown(msg)

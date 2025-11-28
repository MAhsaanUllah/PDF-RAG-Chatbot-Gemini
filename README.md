# 📄 PDF-RAG-Chatbot-Gemini

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)](https://www.langchain.com/)  
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-00BCD4)](https://ai.google/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Live App](https://img.shields.io/badge/💻-Open%20App-blue?style=for-the-badge)](https://pdf-rag-chatbot-gemini-gds.streamlit.app/?embed_options=dark_theme)

💬 *"Ask your PDFs anything — powered by Google Gemini & LangChain magic."*

A **Retrieval-Augmented Generation (RAG) chatbot** that lets users **upload PDFs and interact directly with their content**.  
Built with **LangChain**, **FAISS vector search**, and **Google Gemini API**, all wrapped in an **interactive Streamlit UI**.

---

## 🚀 Features

- 📂 Upload any PDF document for instant analysis  
- 🔍 Context-aware **Q&A retrieval** from documents  
- 🧠 **RAG pipeline** powered by FAISS vector store  
- 🤖 **Google Gemini API** for intelligent responses  
- 💻 Clean & interactive **Streamlit interface**  
- 🔒 API key management via `.env` for security

---

## 🌐 Live Demo

Click the badge to access the live app:

[![Open App](https://img.shields.io/badge/💻-Open%20App-blue?style=for-the-badge)](https://pdf-rag-chatbot-gemini-gds.streamlit.app/?embed_options=dark_theme)

![App Preview](screenshot.png)

---

## 📁 Folder Structure

PDF-RAG-Chatbot-Gemini/
│── app.py # Main Streamlit application
│── requirements.txt # Python dependencies
│── .env # Environment variables (ignored by Git)
│── .env.example # Example env file for reference
│── screenshot.png # App screenshot
└── README.md # Project documentation

yaml
Copy code

---

## 🔑 Environment Variables

Before running the app, create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
Or simply copy .env.example → rename it .env → add your Gemini key.

⚙️ Installation & Usage
1️⃣ Clone the Repository

bash
Copy code
git clone https://github.com/<your-username>/PDF-RAG-Chatbot-Gemini.git
cd PDF-RAG-Chatbot-Gemini
2️⃣ Install Dependencies

bash
Copy code
pip install -r requirements.txt
3️⃣ Set Up Environment Variables

bash
Copy code
cp .env.example .env
# then add your GEMINI_API_KEY inside .env
4️⃣ Run the App

bash
Copy code
streamlit run app.py
🔮 Future Improvements
📚 Multi-PDF support for cross-document Q&A

🗂 Save & reload previous chat history

🌐 Deployment on Hugging Face Spaces & Streamlit Cloud

🔍 Hybrid retrieval (semantic + keyword search)

📜 License
Licensed under the MIT License. Free for use and modification.

This project demonstrates:

RAG Pipeline Skills → Combining LangChain, FAISS, and Gemini for contextual Q&A

Deployment-Ready Design → Environment variable setup + Streamlit UI

Practical Application → A chatbot that transforms static PDFs into interactive knowledge sources

🔗 Relevant for AI Engineer, NLP Engineer, and Data Scientist roles involving LLMs & retrieval systems.

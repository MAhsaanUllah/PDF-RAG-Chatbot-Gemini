import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    google_api_key=google_api_key
)

response = llm.invoke("Hello! Can you explain AI?")
print(response)

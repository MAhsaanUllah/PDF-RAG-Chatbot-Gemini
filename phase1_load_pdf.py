import os
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(path):
    """Load and return full text from a PDF file"""
    text = ""
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def clean_text(text):
    """Remove extra spaces and empty lines"""
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip() != '']
    return '\n'.join(lines)

def split_text(text, chunk_size=500, chunk_overlap=50):
    """Split cleaned text into overlapping chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # replace with your PDF name
    print("🔍 Loading PDF...")
    text = load_pdf(pdf_path)
    
    print("🧹 Cleaning text...")
    cleaned = clean_text(text)
    
    print("🔪 Splitting into chunks...")
    chunks = split_text(cleaned)
    
    print(f"✅ Done! Total chunks: {len(chunks)}")
    print(chunks[:3])  # Show first 3 chunks

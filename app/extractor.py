import os
import requests
from bs4 import BeautifulSoup

def from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def from_pdf(file_path: str) -> str:
    import PyPDF2
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def from_docx(file_path: str) -> str:
    import docx
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def from_website(url: str) -> str:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup(['nav', 'footer', 'script', 'style']):
        tag.decompose()
    text = soup.get_text(separator='\n')
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())[:5000]

def load_all(knowledge_folder: str = "knowledge", website_url: str = None) -> str:
    all_text = ""
    if os.path.exists(knowledge_folder):
        for filename in os.listdir(knowledge_folder):
            filepath = os.path.join(knowledge_folder, filename)
            if filename.endswith('.txt'):
                all_text += from_txt(filepath) + "\n"
            elif filename.endswith('.pdf'):
                all_text += from_pdf(filepath) + "\n"
            elif filename.endswith('.docx'):
                all_text += from_docx(filepath) + "\n"
    if website_url:
        all_text += from_website(website_url) + "\n"
    return all_text
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.1-8b-instant"

    COMPANY_NAME = "Community Healthcare Network"
    AGENT_NAME = "Community Healthcare AI"

    # Knowledge base settings
    SIMPLE_MODE_WORD_LIMIT = 4000
    RAG_CHUNK_SIZE = 200
    RAG_TOP_K = 3
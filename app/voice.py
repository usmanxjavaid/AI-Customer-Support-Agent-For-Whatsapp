import requests
from groq import Groq
from app.logger import logger
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

def transcribe_audio(audio_url: str, auth: tuple) -> str:
    """Downloads audio from Twilio and converts speech to text using Groq Whisper"""
    try:
        response = requests.get(audio_url, auth=auth)
        with open("temp_audio.ogg", "wb") as f:
            f.write(response.content)

        with open("temp_audio.ogg", "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3"
            )
        return transcription.text

    except Exception as e:
        logger.error(f"Transcription failed: {e}")
        return ""
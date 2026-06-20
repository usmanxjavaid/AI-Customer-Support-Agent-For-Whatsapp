from twilio.rest import Client
from app.logger import logger
from config import Config

client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

def send_message(to: str, body: str):
    try:
        client.messages.create(
            from_=Config.TWILIO_WHATSAPP_NUMBER,
            to=to,
            body=body
        )
        logger.info(f"Message sent to {to}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
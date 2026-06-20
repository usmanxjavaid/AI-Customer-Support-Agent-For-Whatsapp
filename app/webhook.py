from fastapi import APIRouter, Request, Form
from fastapi.responses import PlainTextResponse
from app.ai import get_ai_reply
from app.memory import get_history, add_message
from app.whatsapp import send_message
from app.voice import transcribe_audio
from app.logger import logger
from config import Config

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(None),
    NumMedia: str = Form("0"),
    MediaUrl0: str = Form(None)
):
    user_id = From
    logger.info(f"Message from {user_id}: {Body}")

    # Handle voice message
    if int(NumMedia) > 0 and MediaUrl0:
        auth = (Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
        user_message = transcribe_audio(MediaUrl0, auth)
        if not user_message:
            send_message(user_id, "Sorry, I couldn't understand the voice message.")
            return PlainTextResponse("")
    else:
        user_message = Body

    history = get_history(user_id)
    reply = get_ai_reply(user_message, history)

    add_message(user_id, "user", user_message)
    add_message(user_id, "assistant", reply)

    send_message(user_id, reply)
    return PlainTextResponse("")
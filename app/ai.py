from groq import Groq
from app.knowledge import get_context
from app.logger import logger
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

def get_ai_reply(user_message: str, history: list) -> str:
    try:
        context = get_context(user_message)

        system_prompt = f"""You are {Config.AGENT_NAME}, a support assistant for {Config.COMPANY_NAME}.

Use ONLY the information below to answer questions.
If the answer isn't in the information, say "Let me connect you with our team for that."
Keep replies under 80 words.

INFORMATION:
{context}"""

        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(history)
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model=Config.GROQ_MODEL,
            messages=messages,
            max_tokens=200
        )

        reply = response.choices[0].message.content.strip()
        return reply if reply else "Could you rephrase that?"

    except Exception as e:
        logger.error(f"AI reply failed: {e}")
        return "I'm having a technical issue. Please try again."
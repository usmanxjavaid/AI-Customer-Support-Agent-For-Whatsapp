from fastapi import FastAPI
from app.webhook import router
from app.knowledge import initialize_knowledge
from app.logger import logger

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup():
    initialize_knowledge()
    logger.info("WhatsApp AI Agent started")

@app.get("/")
def home():
    return {"status": "running"}
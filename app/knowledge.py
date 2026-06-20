from app.extractor import load_all
from app.rag.chunker import chunk_text
from app.rag.vector_store import store_chunks, search_chunks
from app.logger import logger
from config import Config

knowledge_mode = "simple"
full_text = ""

def initialize_knowledge(website_url: str = None):
    global knowledge_mode, full_text
    full_text = load_all(website_url=website_url)
    word_count = len(full_text.split())

    if word_count <= Config.SIMPLE_MODE_WORD_LIMIT:
        knowledge_mode = "simple"
        logger.info(f"Knowledge loaded: {word_count} words - SIMPLE mode")
    else:
        knowledge_mode = "rag"
        chunks = chunk_text(full_text, Config.RAG_CHUNK_SIZE)
        store_chunks(chunks)
        logger.info(f"Knowledge loaded: {word_count} words - RAG mode ({len(chunks)} chunks)")

def get_context(user_query: str) -> str:
    if knowledge_mode == "simple":
        return full_text
    else:
        chunks = search_chunks(user_query, Config.RAG_TOP_K)
        return "\n\n".join(chunks)
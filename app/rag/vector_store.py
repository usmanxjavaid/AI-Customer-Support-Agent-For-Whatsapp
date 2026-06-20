import chromadb
from app.rag.embedder import get_embedding, get_embeddings
from app.logger import logger

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="knowledge")

def store_chunks(chunks: list):
    """Stores text chunks as vectors in ChromaDB"""
    if not chunks:
        return
    embeddings = get_embeddings(chunks)
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        documents=chunks
    )
    logger.info(f"Stored {len(chunks)} chunks in vector store")

def search_chunks(query: str, top_k: int = 3) -> list:
    """Finds most relevant chunks for a query"""
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0] if results['documents'] else []
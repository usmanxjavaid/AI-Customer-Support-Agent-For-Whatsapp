def chunk_text(text: str, chunk_size: int = 200) -> list:
    """Splits text into chunks of approximately chunk_size words"""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks
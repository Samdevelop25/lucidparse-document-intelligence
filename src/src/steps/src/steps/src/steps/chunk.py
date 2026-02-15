def chunk_text(text: str, max_chars: int = 1200):
    text = text or ""
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i + max_chars])
        i += max_chars
    return chunks

from app.embedder import embed_text
from app.chroma_loader import collection

def query_resume(query: str, top_k: int = 5):
    query_embedding = embed_text(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

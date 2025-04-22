from app.embedder import embed_text
from app.chroma_loader import collection

def query_resume(query_embedding, top_k = 3):

    # Getting resume matches from ChromaDB

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results

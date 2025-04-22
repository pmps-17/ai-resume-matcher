from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list:

    # Getting embeddings from text using SentenceTransformer model
    embedding = model.encode([text])[0]
    return embedding.tolist()  

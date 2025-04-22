import chromadb
from chromadb.config import Settings

client = chromadb.Client()

collection = client.get_or_create_collection(name="resumes")

# Adding resume embeddings to ChromaDB
def add_resume(id: str, content: str, embedding: list):
    collection.add(
        ids=[id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{"source": "resume"}]
    )
    print(f"✅ Resume {id} added to vector DB.")

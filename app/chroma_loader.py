import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())

collection = client.get_or_create_collection(name="resumes")

def add_resume(id: str, content: str, embedding: list):
    collection.add(
        ids=[id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{"source": "resume"}]
    )
    print(f"✅ Resume {id} added to vector DB.")

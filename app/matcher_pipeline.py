from app.embedder import embed_text
from app.chroma_loader import collection
from app.query_engine import query_resume
from app.scorer import score_resume

def match_resumes(query: str):
    query_vector = embed_text(query)
    retrieved = query_resume(query_vector, top_k=5)

    results = []
    for doc, resume_id in zip(retrieved["documents"][0], retrieved["ids"][0]):
        score = score_resume(doc, query)
        results.append({"id": resume_id, "resume": doc, "llm_score": score})

    return results

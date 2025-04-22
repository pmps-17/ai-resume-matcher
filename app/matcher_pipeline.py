from app.embedder import embed_text
from app.query_engine import query_resume
from app.scorer import score_resume

def match_resumes(query: str, top_k: int):
    # Getting embeddings of recruiter query
    query_vector = embed_text(query)

    # Getting resume matches from ChromaDB
    retrieved = query_resume(query_vector, top_k)

    results = []
    for doc, resume_id in zip(retrieved["documents"][0], retrieved["ids"][0]):
        # Evaluating the score from openAI and getting evaluation results
        evaluation = score_resume(doc, query)
        results.append({"id": resume_id, "resume": doc, "llm_score": evaluation.get("score"),
            "llm_reason": evaluation.get("reason")})

    return results

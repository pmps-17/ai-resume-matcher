import pytest
from app.matcher_pipeline import match_resumes

def test_match_resumes_with_top_k(monkeypatch):
    # Dummy data
    docs = ["doc_a", "doc_b", "doc_c"]
    ids  = ["id_a", "id_b", "id_c"]

    # Patch query_resume to return our dummy lists
    monkeypatch.setattr(
        'app.matcher_pipeline.query_resume',
        lambda q, top_k: {"documents": [docs[:top_k]], "ids": [ids[:top_k]]}
    )

    # Patch score_resume to return a predictable dict
    monkeypatch.setattr(
        'app.matcher_pipeline.score_resume',
        lambda doc, q: {"score": len(doc), "reason": f"len={len(doc)}"}
    )

    # Call with top_k = 2
    matches = match_resumes("dummy query", top_k=2)

    # We should get exactly 2 matches back
    assert len(matches) == 2

    # IDs and scores should match our dummy logic
    assert matches[0]["id"] == "id_a"
    assert matches[0]["llm_score"] == len("doc_a")
    assert matches[0]["llm_reason"] == "len=5"

    assert matches[1]["id"] == "id_b"
    assert matches[1]["llm_score"] == len("doc_b")
    assert matches[1]["llm_reason"] == "len=5"

import pytest
from app.embedder import embed_text

def test_embed_text_length():
    text = "This is a test sentence for embedding."
    vec = embed_text(text)
    # Expect a non-empty list of floats
    assert isinstance(vec, list)
    assert all(isinstance(x, float) for x in vec)
    # Typical SBERT models produce 384-dimensional vectors
    assert len(vec) == 384

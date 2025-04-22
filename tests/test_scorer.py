# tests/test_scorer.py

import pytest
import json
from app import scorer

class DummyResponse:
    def __init__(self, content):
        # choices is a list of objects with a .message.content attribute
        Message = type("M", (), {"content": content})
        Choice  = type("C", (), {"message": Message})
        self.choices = [Choice()]

class DummyClient:
    def __init__(self, response_text):
        self.response_text = response_text
        # Expose chat and completions as attributes, not methods
        self.chat = self
        self.completions = self

    def create(self, **kwargs):
        # Return DummyResponse with JSON string
        return DummyResponse(self.response_text)

@pytest.fixture(autouse=True)
def patch_openai(monkeypatch):
    dummy_json = json.dumps({"score": 8, "reason": "Good match."})
    dummy_client = DummyClient(dummy_json)
    # Replace the OpenAI client in your scorer module
    monkeypatch.setattr(scorer, 'client', dummy_client)
    return dummy_client

def test_score_resume_parses_json():
    resume = "Experience in Python and AI."
    query  = "AI developer"
    result = scorer.score_resume(resume, query)
    assert isinstance(result, dict)
    assert result["score"] == 8
    assert "Good match" in result["reason"]

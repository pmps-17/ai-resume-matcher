import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Loading Environment (.env)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Formatting the query and giving it to LLM
def score_resume(resume_text, job_description):
    prompt = f"""
You are an AI assistant that evaluates how well a candidate's resume matches a given job description.
Return your answer in strict JSON with two keys:
  - "score": an integer from 0 to 10
  - "reason": a brief explanation (1–2 sentences)

Job Description:
\"\"\"
{job_description}
\"\"\"

Candidate Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": prompt},
    ],
    temperature=0.3
)

    raw = response.choices[0].message.content.strip()

    # Formatting the response to json for easy retrieval
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"score": None, "reason": raw}

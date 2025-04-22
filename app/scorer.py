import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def score_resume(resume_text, job_description):
    prompt = f"""
You are an AI assistant that helps recruiters match resumes with job descriptions.

Job Description:
\"\"\"
{job_description}
\"\"\"

Candidate Resume:
\"\"\"
{resume_text}
\"\"\"

Evaluate this resume based on skills, experience, and relevance to the job. 
Return a short explanation and a relevance score out of 10.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message["content"]

# index_resumes.py

from app.embedder import embed_text
from app.chroma_loader import add_resume
import os

def main():
    for filename in os.listdir("data/resumes"):
        path = os.path.join("data/resumes", filename)
        with open(path, "r") as f:
            content = f.read()
        embedding = embed_text(content)
        add_resume(filename, content, embedding)
    print("✅ All resumes indexed.")

if __name__ == "__main__":
    main()


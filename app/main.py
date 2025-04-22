
import os
"""To avoid the warning comes from Hugging Face’s tokenizers library 
   detecting that you’ve already spawned worker threads (parallelism) before forking your process, which can deadlock.
"""
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from dotenv import load_dotenv

# 1) Load environment (e.g. OPENAI_API_KEY)
load_dotenv()

import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("resumes")

from app.embedder import embed_text
from app.chroma_loader import add_resume
from app.matcher_pipeline import match_resumes

def index_resumes():
    """
    Walks through resumes and adds its embeddings to the Chroma collection.
    """
    for filename in os.listdir("data/resumes"):
        if not filename.lower().endswith(".txt"):
            continue

        path = os.path.join("data/resumes", filename)
        with open(path, "r") as f:
            content = f.read()

        embedding = embed_text(content)
        add_resume(filename, content, embedding)

    print("✅ Indexed all resumes (in-memory).")

def main():
    # Indexing all resumes
    index_resumes()

    # Ask for recruiter query and number of desired profiles
    query = input("\nEnter job description or query:\n> ").strip()
    top_k = int(input("\nEnter number of desired profiles:\n> "))

    if not query:
        print("No query entered, exiting.")
        return
    if not top_k:
        top_k = 3

    # Retrieve & score matches
    matches = match_resumes(query, top_k)

    # Display top matches
    print(f"\n🔍 Top {len(matches)} Matches:\n")
    for i, match in enumerate(matches, start=1):
        print(f"--- Match #{i} ---")
        print("ID:   ", match["id"])
        print("Score:", match.get("llm_score", "N/A"))
        print("Reason:", match["llm_reason"])
        print("Resume snippet:")
        print(match["resume"][:200].replace("\n", " "), "…\n")

if __name__ == "__main__":
    main()

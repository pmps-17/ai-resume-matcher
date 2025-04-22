from app.matcher_pipeline import match_resumes

if __name__ == "__main__":
    query = input("Enter job description or query: ")
    matches = match_resumes(query)

    for match in matches:
        print("\nID:", match["id"])
        print("Score:", match["llm_score"])
        print("Resume:", match["resume"][:200], "...")

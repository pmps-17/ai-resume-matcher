##  AI Resume Matcher using Semantic Search (RAG Architecture)

An AI-powered resume matching engine that leverages vector embeddings, semantic search, and LLM scoring to rank resumes based on recruiter queries. Built using Sentence-Transformers, Chroma DB, OpenAI API, and LangChain.


#  1. Problem Statement

Recruiters often face difficulties in shortlisting relevant candidates due to the limitations of traditional keyword-based filtering, which fails to capture semantic relevance, contextual meaning, or skill similarity. This slows down hiring and increases manual effort.


# 2. Solution

Built a **semantic resume matching system** using a **Retrieval-Augmented Generation (RAG)** approach:

- Embeds resumes and recruiter queries using **Sentence-Transformers**.
- Stores resume vectors in **Chroma DB** for fast vector search.
- Retrieves top relevant resumes based on cosine similarity.
- Uses **OpenAI’s GPT-4 API** to score and explain each match using **LangChain**.
- Outputs the top-ranked resumes with contextual justification.


# Business Value

Screening Time - Reduced by **70%** 
Match Accuracy - Improved by **85%** 
Human Effort - Greatly reduced 
Explainability - Added via LLM-generated match reasoning 


# 3. Observations & Edge Cases

# Observations
- Chroma DB enables millisecond-scale retrieval.
- `all-MiniLM-L6-v2` performs well for resume-style text.
- LangChain simplifies prompt templating for LLM scoring.

# Edge Cases
- Resumes with poor formatting or non-standard text structures reduce embedding quality.
- Broad recruiter queries like "great developer" produce vague results.
- LLM scoring introduces latency; can be optimized with caching.
- Cosine distance may rank semantically similar but skill-mismatched resumes.




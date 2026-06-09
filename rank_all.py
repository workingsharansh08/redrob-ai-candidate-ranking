import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

results = []

for candidate in candidates:

    score = 0

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    headline = profile["headline"].lower()
    summary = profile["summary"].lower()

    # -------------------
    # EXPERIENCE
    # -------------------

    exp = profile["years_of_experience"]

    if 5 <= exp <= 9:
        score += 20
    elif 4 <= exp <= 10:
        score += 10

    # -------------------
    # OPEN TO WORK
    # -------------------

    if signals["open_to_work_flag"]:
        score += 10

    # -------------------
    # RECRUITER SIGNALS
    # -------------------

    score += signals["recruiter_response_rate"] * 10
    score += signals["interview_completion_rate"] * 10
    score += signals["github_activity_score"] * 0.2

    # -------------------
    # PROFESSION RELEVANCE
    # -------------------

    good_terms = [
        "machine learning",
        "ml engineer",
        "ai engineer",
        "search",
        "retrieval",
        "ranking",
        "recommendation",
        "nlp",
        "llm",
        "applied ml"
    ]

    for term in good_terms:
        if term in headline or term in summary:
            score += 10

    # -------------------
    # BAD PROFILES
    # -------------------

    bad_terms = [
        "accountant",
        "marketing",
        "hr",
        "sales",
        "graphic designer",
        "customer support",
        "operations manager",
        "recruiter"
    ]

    for term in bad_terms:
        if term in headline or term in summary:
            score -= 25

    # -------------------
    # SKILLS
    # -------------------

    skills = [
        skill["name"].lower()
        for skill in candidate["skills"]
    ]

    important_skills = [
        "pinecone",
        "faiss",
        "milvus",
        "embeddings",
        "information retrieval",
        "sentence transformers",
        "machine learning",
        "nlp",
        "fine-tuning llms",
        "weaviate",
        "qdrant"
    ]

    for skill in important_skills:
        if skill in skills:
            score += 6

    # -------------------
    # CAREER EVIDENCE
    # -------------------

    career_text = ""

    for job in candidate["career_history"]:
        career_text += job["description"].lower() + " "

    evidence_keywords = [
        "ranking",
        "retrieval",
        "recommendation",
        "search",
        "embeddings",
        "evaluation",
        "a/b",
        "offline-online",
        "xgboost",
        "lightgbm",
        "learning-to-rank",
        "feature engineering",
        "relevance",
        "production",
        "shipped"
    ]

    evidence_score = 0

    for keyword in evidence_keywords:
        if keyword in career_text:
            evidence_score += 8

    score += evidence_score

    # -------------------
    # PRODUCT COMPANIES
    # -------------------

    product_companies = [
        "swiggy",
        "zomato",
        "uber",
        "flipkart",
        "amazon",
        "google",
        "microsoft",
        "mad street den"
    ]

    for job in candidate["career_history"]:
        company = job["company"].lower()
        if company in product_companies:
            score += 15

    # -------------------
    # FAKE AI PENALTY
    # -------------------

    ai_skills_present = False

    fake_ai_skills = [
        "pinecone",
        "faiss",
        "embeddings",
        "langchain",
        "vector search",
        "fine-tuning llms",
        "recommendation systems"
    ]

    for skill in skills:
        if skill in fake_ai_skills:
            ai_skills_present = True

    real_ai_evidence = False

    for keyword in evidence_keywords:
        if keyword in career_text:
            real_ai_evidence = True

    if ai_skills_present and not real_ai_evidence:
        score -= 40

    # -------------------
    # CONSULTING COMPANY PENALTY
    # -------------------

    consulting_companies = [
        "tcs",
        "infosys",
        "wipro",
        "cognizant",
        "capgemini",
        "accenture"
    ]

    consulting_count = 0

    for job in candidate["career_history"]:
        if job["company"].lower() in consulting_companies:
            consulting_count += 1

    if consulting_count >= 2:
        score -= 15

    # -------------------

    results.append({
        "id": candidate["candidate_id"],
        "score": round(score, 2),
        "headline": profile["headline"]
    })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for i, candidate in enumerate(results[:10], start=1):
    print(
        f"{i}. {candidate['id']} | "
        f"{candidate['score']} | "
        f"{candidate['headline']}"
    )
    results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for i, candidate in enumerate(results[:10], start=1):
    print(
        f"{i}. {candidate['id']} | "
        f"{candidate['score']} | "
        f"{candidate['headline']}"
    )

# ----------------------------------
# EXPORT RANKED OUTPUT FILE
# ----------------------------------

import csv

with open("ranked_candidates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "rank",
        "candidate_id",
        "score"
    ])

    for rank, candidate in enumerate(results, start=1):
        writer.writerow([
            rank,
            candidate["id"],
            candidate["score"]
        ])

print("\nranked_candidates.csv created successfully")
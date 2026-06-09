import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate_id = "CAND_0000031"

for c in candidates:

    if c["candidate_id"] == candidate_id:

        reasons = []

        headline = c["profile"]["headline"].lower()
        summary = c["profile"]["summary"].lower()

        # Relevance reasons
        keywords = [
            "search",
            "retrieval",
            "ranking",
            "recommendation",
            "machine learning",
            "nlp",
            "llm"
        ]

        for keyword in keywords:
            if keyword in headline or keyword in summary:
                reasons.append(f"Strong {keyword} experience")

        # Skills
        skills = [s["name"] for s in c["skills"]]

        important_skills = [
            "Pinecone",
            "FAISS",
            "Embeddings",
            "Information Retrieval",
            "Sentence Transformers",
            "Machine Learning"
        ]

        for skill in important_skills:
            if skill in skills:
                reasons.append(f"Has skill: {skill}")

        # Product companies
        good_companies = [
            "Swiggy",
            "Uber",
            "Zomato"
        ]

        for job in c["career_history"]:
            if job["company"] in good_companies:
                reasons.append(
                    f"Product company experience ({job['company']})"
                )

        print("\n========================")
        print("CANDIDATE SUMMARY")
        print("========================\n")

        print("ID:", c["candidate_id"])
        print("Headline:", c["profile"]["headline"])
        print("Company:", c["profile"]["current_company"])
        print("Experience:", c["profile"]["years_of_experience"], "years")

        print("\nReasons:")

        for reason in reasons:
            print("✓", reason)

        break
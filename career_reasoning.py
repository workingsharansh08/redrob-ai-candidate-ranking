import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate_id = "CAND_0000031"

for c in candidates:

    if c["candidate_id"] == candidate_id:

        career_text = ""

        for job in c["career_history"]:
            career_text += job["description"].lower()

        signals = {
            "ranking models": "Built ranking systems",
            "recommendation": "Recommendation experience",
            "retrieval": "Retrieval experience",
            "search": "Search experience",
            "a/b": "A/B testing experience",
            "offline-online": "Evaluation framework experience",
            "xgboost": "Learning-to-rank experience",
            "lightgbm": "Learning-to-rank experience",
            "embeddings": "Embedding systems experience"
        }

        print("\nCAREER EVIDENCE\n")

        for key, value in signals.items():
            if key in career_text:
                print("✓", value)

        break
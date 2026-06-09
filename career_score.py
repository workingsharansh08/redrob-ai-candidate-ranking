import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[30]  # candidate 31

career_text = ""

for job in candidate["career_history"]:
    career_text += job["description"].lower() + " "

keywords = [
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embeddings",
    "vector",
    "pinecone",
    "faiss",
    "evaluation",
    "a/b",
    "xgboost",
    "lightgbm"
]

score = 0

for keyword in keywords:
    if keyword in career_text:
        score += 10

print("Career Score:", score)
import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

for c in candidates:
    if c["candidate_id"] == "CAND_0000031":
        print(c)
        break
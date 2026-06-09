import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

target_id = "CAND_0000016"

for c in candidates:
    if c["candidate_id"] == target_id:
        print(c)
        break
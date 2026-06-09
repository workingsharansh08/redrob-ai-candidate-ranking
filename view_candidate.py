import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total candidates:", len(data))

print("\nFIRST CANDIDATE:\n")

print(data[0])
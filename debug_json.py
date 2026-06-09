import json

try:
    with open("sample_candidates.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("JSON loaded successfully!")
    print("Candidates:", len(data))

except Exception as e:
    print("ERROR:")
    print(e)
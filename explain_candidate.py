import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate_id = "CAND_0000031"

for c in candidates:

    if c["candidate_id"] == candidate_id:

        print("\nCANDIDATE REPORT\n")

        print("Headline:")
        print(c["profile"]["headline"])

        print("\nCompany:")
        print(c["profile"]["current_company"])

        print("\nExperience:")
        print(c["profile"]["years_of_experience"])

        print("\nTop Skills:")

        for skill in c["skills"][:10]:
            print("-", skill["name"])

        print("\nCareer History:")

        for job in c["career_history"]:
            print("\n---")
            print(job["title"])
            print(job["company"])
            print(job["description"])

        break
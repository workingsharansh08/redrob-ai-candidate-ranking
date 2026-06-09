import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

candidate = data[0]

skills = []

for skill in candidate["skills"]:
    skills.append(skill["name"])

career_text = ""

for job in candidate["career_history"]:
    career_text += job["description"] + "\n"

candidate_text = f"""
Headline:
{candidate["profile"]["headline"]}

Summary:
{candidate["profile"]["summary"]}

Skills:
{", ".join(skills)}

Career:
{career_text}
"""

print(candidate_text)

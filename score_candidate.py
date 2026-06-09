import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

candidate = data[0]

score = 0

# Experience
exp = candidate["profile"]["years_of_experience"]

if 5 <= exp <= 9:
    score += 20

# Open to work
if candidate["redrob_signals"]["open_to_work_flag"]:
    score += 10

# Recruiter response rate
score += candidate["redrob_signals"]["recruiter_response_rate"] * 20

# Interview completion
score += candidate["redrob_signals"]["interview_completion_rate"] * 20

# GitHub activity
score += candidate["redrob_signals"]["github_activity_score"]

skills = [
    skill["name"].lower()
    for skill in candidate["skills"]
]

important_skills = [
    "milvus",
    "nlp",
    "fine-tuning llms",
    "apache beam"
]

for skill in important_skills:
    if skill in skills:
        score += 5

print("Candidate:", candidate["candidate_id"])
print("Score:", round(score, 2))
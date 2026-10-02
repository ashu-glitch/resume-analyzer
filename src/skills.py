import csv
import re

from src.parser import clean_text


def load_skills(path="data/skills.csv"):
    """Read the skills list from a CSV file (one skill per line)."""
    skills = []
    with open(path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if row and row[0].strip():
                skills.append(row[0].strip())
    return skills


def find_skills(cleaned_text, skills):
    """Return the set of skills found in already-cleaned text."""
    found = set()
    for skill in skills:
        pattern = (
            r"(?<![a-z0-9+#])"
            + re.escape(clean_text(skill))
            + r"(?![a-z0-9+#])"
        )
        if re.search(pattern, cleaned_text):
            found.add(skill)
    return found


def compare_skills(resume_text, job_text, skills):
    """Return (matched, missing, all_resume_skills), all as sorted lists."""
    resume_skills = find_skills(resume_text, skills)
    job_skills = find_skills(job_text, skills)
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    return matched, missing, sorted(resume_skills)
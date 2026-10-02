from src.parser import extract_text_from_pdf, clean_text
from src.skills import load_skills, compare_skills

job = """
We are looking for an AI/ML intern with strong Python skills.
Experience with machine learning, scikit-learn, TensorFlow, pandas
and numpy is required. Knowledge of NLP, SQL, Git and Docker is a plus.
"""

skills = load_skills()
resume = clean_text(extract_text_from_pdf("resume.pdf"))
job = clean_text(job)

matched, missing, resume_skills = compare_skills(resume, job, skills)

print("Skills found in resume:", resume_skills)
print()
print("Matched skills:", matched)
print("Missing skills:", missing)
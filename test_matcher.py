from src.parser import extract_text_from_pdf, clean_text
from src.matcher import tfidf_score

job = """
We are looking for an AI/ML intern with strong Python skills.
Experience with machine learning, scikit-learn, TensorFlow, pandas
and numpy is required. Knowledge of NLP, SQL, Git and Docker is a plus.
"""

resume = clean_text(extract_text_from_pdf("resume.pdf"))
job = clean_text(job)

print("Match score:", tfidf_score(resume, job), "%")
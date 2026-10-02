from src.parser import extract_text_from_pdf
from src.matcher import tfidf_score, semantic_score

job = """
We are looking for an AI/ML intern with strong Python skills.
Experience with machine learning, scikit-learn, TensorFlow, pandas
and numpy is required. Knowledge of NLP, SQL, Git and Docker is a plus.
"""

resume = extract_text_from_pdf("resume.pdf")

print("Keyword (TF-IDF) score:", tfidf_score(resume, job))
print("Semantic score:", semantic_score(resume, job))
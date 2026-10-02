from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

_model = None


def _get_model():
    """Load the Sentence-BERT model once (downloads on first use)."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _chunk(text: str, size: int = 120):
    """Split text into chunks of about `size` words."""
    words = text.split()
    chunks = [" ".join(words[i:i + size]) for i in range(0, len(words), size)]
    return chunks or [""]


def tfidf_score(resume_text: str, job_text: str) -> float:
    """Keyword similarity (0-100): counts shared words."""
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(float(score) * 100, 2)


def semantic_score(resume_text: str, job_text: str) -> float:
    """Meaning similarity (0-100): for each part of the job description,
    find the best-matching part of the resume, then average."""
    model = _get_model()
    resume_emb = model.encode(_chunk(resume_text), normalize_embeddings=True)
    job_emb = model.encode(_chunk(job_text), normalize_embeddings=True)
    sims = cosine_similarity(job_emb, resume_emb)
    best_per_job_chunk = sims.max(axis=1)
    score = max(float(best_per_job_chunk.mean()), 0.0)
    return round(score * 100, 2)
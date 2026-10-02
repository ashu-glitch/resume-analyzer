# AI Resume Analyzer & Job Matcher

An NLP-based tool that compares a resume with a job description and tells you how well they match, which skills you already have, and which ones you are missing.

## Demo
![App screenshot](docs/screenshot.png)

**Scoring:** Overall match = 50% skill match + 30% semantic match (Sentence-BERT) + 20% keyword match (TF-IDF).

## Features
- Upload a resume in PDF format
- Paste any job description
- Get an overall match score (0-100%)
- See matched skills and missing skills
- Get suggestions to improve your resume

## How it works
1. Extracts text from the resume PDF
2. Cleans and processes the text
3. Finds known skills in both the resume and the job description
4. Compares meaning with Sentence-BERT and shared words with TF-IDF
5. Combines everything into one score and shows it in a Streamlit app

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tech Stack
Python, pdfplumber, scikit-learn, Sentence-Transformers, Streamlit

## Status
Working prototype. Next: online deployment.

## Author
Ashutosh Mishra

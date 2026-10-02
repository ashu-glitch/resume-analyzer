import streamlit as st

from src.parser import extract_text_from_pdf, clean_text
from src.matcher import tfidf_score, semantic_score
from src.skills import load_skills, compare_skills

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

st.title("📄 AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and paste a job description to see how well they match.")

uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description here", height=220)

if st.button("Analyze", type="primary"):
    if uploaded is None or not job_description.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        raw_text = extract_text_from_pdf(uploaded)

        if not raw_text.strip():
            st.error(
                "Could not read any text from this PDF. "
                "It may be a scanned image. Try a PDF exported from Word or Google Docs."
            )
        else:
            with st.spinner("Analyzing (the first run loads the AI model)..."):
                resume = clean_text(raw_text)
                job = clean_text(job_description)

                skills = load_skills()
                matched, missing, resume_skills = compare_skills(resume, job, skills)

                keyword_score = tfidf_score(resume, job)
                meaning_score = semantic_score(raw_text, job_description)

            total_job_skills = len(matched) + len(missing)
            if total_job_skills:
                skill_score = len(matched) / total_job_skills * 100
                final_score = round(
                    0.5 * skill_score + 0.3 * meaning_score + 0.2 * keyword_score, 1
                )
            else:
                skill_score = None
                final_score = round(0.6 * meaning_score + 0.4 * keyword_score, 1)

            st.subheader("Results")
            st.metric("Overall match", f"{final_score}%")
            st.progress(min(int(final_score), 100))

            c1, c2, c3 = st.columns(3)
            c1.metric(
                "Skill match",
                f"{round(skill_score, 1)}%" if skill_score is not None else "n/a",
            )
            c2.metric("Semantic match", f"{meaning_score}%")
            c3.metric("Keyword match", f"{keyword_score}%")

            if skill_score is None:
                st.caption(
                    "No known skills were found in this job description, "
                    "so the overall score uses only semantic and keyword matching."
                )

            left, right = st.columns(2)
            with left:
                st.markdown("### ✅ Matched skills")
                if matched:
                    for s in matched:
                        st.write(f"- {s}")
                else:
                    st.write("No matching skills found.")
            with right:
                st.markdown("### ❌ Missing skills")
                if missing:
                    for s in missing:
                        st.write(f"- {s}")
                else:
                    st.write("You cover every skill the job asks for.")

            if missing:
                st.markdown("### 💡 Suggestions")
                st.info(
                    "Add these skills to your resume (only if you actually have them), "
                    "ideally inside a project or experience bullet: "
                    + ", ".join(missing)
                )
import streamlit as st
from backend.parser import extract_text_from_pdf
from backend.ats import calculate_ats_score
from backend.llm import analyze_resume_with_ai
from backend.report import create_pdf
from backend.similarity import calculate_similarity
from backend.evaluator import evaluate_resume

from ui.sidebar import show_sidebar
from ui.uploader import upload_resume
from ui.dashboard import show_dashboard
from ui.charts import show_skill_chart
from ui.feedback import show_ai_feedback

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

show_sidebar()

st.title("🤖 AI Resume Analyzer")

st.caption(
    "Analyze your resume using ATS scoring and Gemini AI."
)

st.divider()

uploaded_file = upload_resume()

resume_text = ""

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

# -----------------------------
# Job Description
# -----------------------------
st.divider()
st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the Job Description Here",
    height=200,
    placeholder="Paste any job description..."
)

analyze = st.button("🔍 Analyze Resume")

# -----------------------------
# Analysis
# -----------------------------
if analyze:

    if uploaded_file is None:
        st.warning("⚠ Please upload your resume.")
        st.stop()

    if job_description.strip() == "":
        st.warning("⚠ Please paste the Job Description.")
        st.stop()

    # ATS Score
    score, matched, missing = calculate_ats_score(
        resume_text,
        job_description
    )

    st.divider()
    st.success("✅ Analysis Complete!")

    show_dashboard(score)
    semantic_score = calculate_similarity(
        resume_text,
        job_description
    )

    st.subheader("🧠 Semantic Match Score")

    st.metric(
        "Similarity",
        f"{semantic_score}%"
    )

    overall_score, sections = evaluate_resume(resume_text)

    st.subheader("📋 Resume Evaluation")

    for section, value in sections.items():
        st.write(f"**{section}**")
        st.progress(value / 100)
        st.caption(f"{value}%")

    st.success(f"Overall Resume Quality: {overall_score}%")

    show_skill_chart(matched, missing)

    # Gemini AI
    st.divider()

    with st.spinner("Analyzing Resume with Gemini..."):

        ai_response = analyze_resume_with_ai(
            resume_text,
            job_description
        )

    show_ai_feedback(ai_response)

    pdf_file = create_pdf(
        score,
        matched,
        missing,
        ai_response
    )

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf"
        )
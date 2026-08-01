import streamlit as st


def show_sidebar():
    with st.sidebar:
        st.title("🤖 AI Resume Analyzer")

        st.markdown("---")

        st.subheader("Features")

        st.markdown("""
- 📄 Resume Upload
- 🎯 ATS Score
- 🤖 Gemini AI Analysis
- 📊 Skill Visualization
- 📄 PDF Report
        """)

        st.markdown("---")

        st.info("Version 2.0")

        st.caption("Built with Python • Streamlit • Gemini")
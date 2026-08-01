import streamlit as st


def upload_resume():
    return st.file_uploader(
        "Choose your Resume (PDF)",
        type=["pdf"],
    )
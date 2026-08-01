import re
SKILLS = [
    "python", "sql", "fastapi", "flask", "django",
    "git", "github", "docker", "kubernetes",
    "aws", "azure", "gcp",
    "machine learning", "deep learning",
    "tensorflow", "pytorch",
    "numpy", "pandas", "scikit-learn",
    "streamlit", "rest api",
    "gen ai", "llm",
    "langchain", "rag",
    "faiss", "chromadb",
    "huggingface",
    "opencv",
    "mongodb",
    "postgresql",
    "redis",
    "linux",
    "ci/cd"
]

def calculate_ats_score(resume_text, job_description):

    resume = resume_text.lower()
    jd = job_description.lower()

    matched = []
    missing = []

    for skill in SKILLS:

        if skill in jd:

            if skill in resume:
                matched.append(skill)

            else:
                missing.append(skill)

    if len(matched) + len(missing) == 0:
        score = 0
    else:
        score = int((len(matched) / (len(matched) + len(missing))) * 100)

    return score, matched, missing
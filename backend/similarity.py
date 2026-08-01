print("similarity.py loaded")
import re


def _tokenize(text):
    return set(re.findall(r"[a-z0-9+#.]+", text.lower()))


def calculate_similarity(resume_text, job_description):
    resume_tokens = _tokenize(resume_text)
    job_tokens = _tokenize(job_description)

    if not resume_tokens or not job_tokens:
        return 0

    overlap = resume_tokens & job_tokens
    union = resume_tokens | job_tokens

    if not union:
        return 0

    similarity = (len(overlap) / len(union)) * 100
    return round(similarity, 2)
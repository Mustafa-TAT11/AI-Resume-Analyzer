import re


def evaluate_resume(resume_text):
    text = resume_text.lower()

    sections = {
        "Technical Skills": 0,
        "Projects": 0,
        "Experience": 0,
        "Education": 0,
        "Keywords": 0,
    }

    # Technical Skills
    tech_keywords = [
        "python", "sql", "fastapi", "streamlit",
        "docker", "aws", "git", "machine learning",
        "pandas", "numpy"
    ]

    matched = sum(1 for skill in tech_keywords if skill in text)
    sections["Technical Skills"] = min(100, matched * 10)

    # Projects
    project_words = ["project", "github", "developed", "built", "implemented"]
    sections["Projects"] = min(
        100,
        sum(20 for word in project_words if word in text)
    )

    # Experience
    experience_words = ["intern", "experience", "worked", "developer"]
    sections["Experience"] = min(
        100,
        sum(25 for word in experience_words if word in text)
    )

    # Education
    education_words = ["b.tech", "btech", "computer science", "cgpa"]
    sections["Education"] = min(
        100,
        sum(25 for word in education_words if word in text)
    )

    # Keywords
    words = re.findall(r"\w+", text)
    sections["Keywords"] = min(100, len(set(words)) // 5)

    overall = int(sum(sections.values()) / len(sections))

    return overall, sections

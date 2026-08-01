import os
import re
from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def _extract_keywords(text):
    tokens = re.findall(r"[a-z0-9+#.]+", text.lower())
    stop_words = {
        "the", "and", "for", "with", "your", "from", "that", "this", "have",
        "will", "into", "about", "using", "experience", "skills", "resume",
        "job", "description", "team", "work", "project", "projects", "role"
    }
    return [token for token in tokens if len(token) > 2 and token not in stop_words]


def _build_fallback_response(resume_text, job_description, error=None):
    resume_keywords = set(_extract_keywords(resume_text))
    job_keywords = [keyword for keyword in _extract_keywords(job_description) if keyword not in resume_keywords]

    matched_keywords = [keyword for keyword in job_keywords if keyword in resume_keywords][:8]
    missing_keywords = [keyword for keyword in job_keywords if keyword not in resume_keywords][:8]

    error_note = f"\n\nNote: Gemini API is currently unavailable ({error})." if error else ""

    return f"""Fallback AI Review

The Gemini API is unavailable right now, so this response was generated locally from the resume and job description.{error_note}

ATS Feedback:
Your resume should be strengthened with more targeted keywords and examples that directly match the role requirements.

Strengths:
The resume already includes some relevant experience and terminology that can support the application.

Weaknesses:
The resume may need clearer alignment with the exact tools, technologies, and responsibilities mentioned in the job description.

Missing Skills:
{', '.join(missing_keywords) if missing_keywords else 'No obvious keyword gaps were detected.'}

Resume Improvement Suggestions:
- Add role-specific keywords naturally throughout the summary and experience sections.
- Emphasize measurable achievements and outcomes.
- Tailor the resume summary for this specific job title.

Keywords to Include:
{', '.join(matched_keywords) if matched_keywords else 'No additional keywords were detected.'}

Overall Rating (/10):
7/10
"""


def analyze_resume_with_ai(resume_text, job_description):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return:

1. ATS Feedback
2. Strengths
3. Weaknesses
4. Missing Skills
5. Resume Improvement Suggestions
6. Projects to Add
7. Keywords to Include
8. Overall Rating (/10)
"""

    if not client:
        return _build_fallback_response(resume_text, job_description, "Google API key is not configured")

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text
    except (genai_errors.ClientError, Exception) as exc:
        return _build_fallback_response(resume_text, job_description, str(exc))
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
ASSETS_DIR = BASE_DIR / "assets"

APP_TITLE = "AI Resume Analyzer"
APP_ICON = "📄"
APP_DESCRIPTION = "Analyze your resume using ATS scoring and Gemini AI to improve your chances of landing interviews."

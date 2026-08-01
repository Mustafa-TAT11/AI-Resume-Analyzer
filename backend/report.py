from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(score, matched, missing, ai_feedback):
    file_name = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))
    elements.append(Paragraph(f"<b>ATS Score:</b> {score}%", styles["BodyText"]))

    elements.append(
        Paragraph(f"<b>Matched Skills:</b> {', '.join(matched)}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"<b>Missing Skills:</b> {', '.join(missing)}", styles["BodyText"])
    )

    elements.append(Paragraph("<b>Gemini AI Feedback</b>", styles["Heading2"]))
    elements.append(Paragraph(ai_feedback.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(elements)

    return file_name
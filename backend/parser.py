import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_file):
    text = ""

    try:
        pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
    except Exception as e:
        return f"Error reading PDF: {e}"

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

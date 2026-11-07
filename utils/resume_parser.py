
from pypdf import PdfReader
from docx import Document
from io import BytesIO


def extract_resume_text(uploaded_file):

    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    if file_name.endswith(".pdf"):

        reader = PdfReader(BytesIO(file_bytes))
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    elif file_name.endswith(".docx"):

        document = Document(BytesIO(file_bytes))

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return text

    else:
        raise ValueError("Only PDF and DOCX files are supported.")

from PyPDF2 import PdfReader
from fastapi import UploadFile


class PDFService:
    """
    Handles PDF resume text extraction.
    """

    def extract_text(self, resume_file: UploadFile) -> str:
        """
        Extract text from uploaded PDF resume.
        """

        reader = PdfReader(resume_file.file)

        text_chunks = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_chunks.append(page_text)

        raw_text = "\n".join(text_chunks)

        return self._clean_text(raw_text)

    def _clean_text(self, text: str) -> str:
        """
        Cleans extracted PDF text.
        """

        # Remove extra spaces
        text = " ".join(text.split())

        # Normalize line breaks
        text = text.replace(" \n ", "\n").strip()

        return text

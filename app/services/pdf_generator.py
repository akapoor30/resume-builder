from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


class PDFGenerator:
    """
    Generates ATS-friendly resume PDFs from plain text.
    """

    def generate_pdf(self, resume_text: str) -> BytesIO:
        """
        Convert resume text into a PDF and return buffer.
        """

        buffer = BytesIO()

        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40,
        )

        styles = getSampleStyleSheet()
        normal_style = styles["Normal"]
        heading_style = ParagraphStyle(
            "HeadingStyle",
            parent=styles["Heading2"],
            spaceAfter=12,
        )

        elements = []

        lines = resume_text.split("\n")

        for line in lines:
            line = line.strip()

            if not line:
                elements.append(Paragraph("<br/>", normal_style))
                continue

            # Headings (simple heuristic)
            if line.isupper() or line.endswith(":"):
                elements.append(Paragraph(line, heading_style))
            # Bullet points
            elif line.startswith("-"):
                bullet = line.replace("-", "").strip()
                elements.append(
                    ListFlowable(
                        [ListItem(Paragraph(bullet, normal_style))],
                        bulletType="bullet",
                        start="circle",
                        leftIndent=20,
                    )
                )
            else:
                elements.append(Paragraph(line, normal_style))

        doc.build(elements)
        buffer.seek(0)

        return buffer

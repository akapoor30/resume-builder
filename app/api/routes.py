from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from typing import List

from app.services.resume_service import ResumeService
from app.services.pdf_generator import PDFGenerator
from app.models.request_models import ResumeCreateRequest

router = APIRouter()
resume_service = ResumeService()
pdf_generator = PDFGenerator()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/resume/refactor")
async def refactor_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...),
    experience_level: str = Form(...),
    role_type: str = Form(...),
    industry: str = Form(...)
):
    """
    Refactor an existing resume PDF based on job description.
    """

    result = await resume_service.refactor_resume(
        resume_file=resume_file,
        job_description=job_description,
        experience_level=experience_level,
        role_type=role_type,
        industry=industry
    )

    pdf_buffer = pdf_generator.generate_pdf(result["resume_text"])

    response = StreamingResponse(
        pdf_buffer,
        media_type="application/pdf"
    )
    response.headers["Content-Disposition"] = "attachment; filename=optimized_resume.pdf"

    # ATS keywords in headers (optional but nice)
    response.headers["X-ATS-Keywords"] = ", ".join(result["ats_keywords"])

    return response


@router.post("/resume/create")
async def create_resume(payload: ResumeCreateRequest):
    """
    Create a resume from scratch.
    """

    result = await resume_service.create_resume(
        candidate_data=payload.dict(),
        job_description=payload.job_description,
        experience_level=payload.experience_level,
        role_type=payload.role_type,
        industry=payload.industry
    )

    pdf_buffer = pdf_generator.generate_pdf(result["resume_text"])

    response = StreamingResponse(
        pdf_buffer,
        media_type="application/pdf"
    )
    response.headers["Content-Disposition"] = "attachment; filename=generated_resume.pdf"
    response.headers["X-ATS-Keywords"] = ", ".join(result["ats_keywords"])

    return response

from typing import Optional, Dict, Any

from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService
from app.services.jd_service import JDService
from app.services.pdf_service import PDFService
from app.utils.resume_sanitizer import ResumeSanitizer



class ResumeService:
    """
    Orchestrates resume creation and refactoring workflows.
    """

    def __init__(self):
        self.prompt_service = PromptService()
        self.llm_service = LLMService()
        self.jd_service = JDService()
        self.pdf_service = PDFService()

    async def refactor_resume(
        self,
        resume_file,
        job_description: str,
        experience_level: str,
        role_type: str,
        industry: str
    ) -> Dict[str, Any]:
        """
        Refactor an existing resume based on job description.
        """

        # 1. Extract resume text from PDF
        resume_text = self.pdf_service.extract_text(resume_file)

        # 2. Analyze job description
        ats_keywords = self.jd_service.extract_keywords(job_description)

        # 3. Build prompt
        context = {
            "experience_level": experience_level,
            "role_type": role_type,
            "industry": industry,
            "job_description": job_description,
            "resume_text": resume_text,
            "candidate_data": None,
        }

        prompt = self.prompt_service.build_prompt(
            mode="refactor",
            context=context
        )

        # 4. Generate resume via LLM
        raw_output = await self.llm_service.generate_resume(prompt)
        sanitized = ResumeSanitizer.sanitize(raw_output)
        final_resume = ResumeStructureEnforcer.enforce(sanitized)



        return {
            "resume_text": resume_output,
            "ats_keywords": ats_keywords
        }

    async def create_resume(
        self,
        candidate_data: Dict[str, Any],
        job_description: str,
        experience_level: str,
        role_type: str,
        industry: str
    ) -> Dict[str, Any]:
        """
        Create a resume from scratch.
        """

        # 1. Analyze job description
        ats_keywords = self.jd_service.extract_keywords(job_description)

        # 2. Build prompt
        context = {
            "experience_level": experience_level,
            "role_type": role_type,
            "industry": industry,
            "job_description": job_description,
            "resume_text": None,
            "candidate_data": candidate_data,
        }

        prompt = self.prompt_service.build_prompt(
            mode="create",
            context=context
        )

        # 3. Generate resume via LLM
        resume_output = await self.llm_service.generate_resume(prompt)

        return {
            "resume_text": resume_output,
            "ats_keywords": ats_keywords
        }

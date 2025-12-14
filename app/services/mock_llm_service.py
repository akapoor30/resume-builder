class MockLLMService:
    """
    Mock LLM service for local development without OpenAI credentials.
    """

    async def generate_resume(self, prompt: str) -> str:
        return """
NAME: Test User
ROLE: Backend Engineer

PROFESSIONAL SUMMARY
Backend Engineer with experience in Python, FastAPI, and SQL.
Strong understanding of REST APIs and backend system design.

SKILLS
- Python
- FastAPI
- SQL
- REST APIs
- Git

PROJECTS
AI Resume Builder
- Built a FastAPI-based backend to generate ATS-optimized resumes.
- Designed modular services following clean architecture principles.

EDUCATION
Bachelor of Technology in Computer Science
"""

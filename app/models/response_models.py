from pydantic import BaseModel
from typing import List

class ResumeResponse(BaseModel):
    resume_text: str
    ats_keywords: List[str]

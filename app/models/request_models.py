from pydantic import BaseModel
from typing import List, Optional

class ResumeCreateRequest(BaseModel):
    candidate_name: str
    experience_level: str
    role_type: str
    industry: str
    skills: List[str]
    projects: Optional[List[dict]] = []
    job_description: str

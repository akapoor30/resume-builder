import re
from typing import List

from app.core.constants import COMMON_SKILLS, SOFT_SKILLS


class JDService:
    """
    Extracts ATS-relevant keywords from job descriptions.
    """

    def extract_keywords(self, job_description: str) -> List[str]:
        """
        Extracts and returns a unique list of keywords.
        """

        text = job_description.lower()

        extracted = set()

        # 1. Extract technical skills
        for skill in COMMON_SKILLS:
            if re.search(rf"\b{re.escape(skill.lower())}\b", text):
                extracted.add(skill)

        # 2. Extract soft skills
        for skill in SOFT_SKILLS:
            if re.search(rf"\b{re.escape(skill.lower())}\b", text):
                extracted.add(skill)

        return sorted(extracted)

from typing import Dict, Any

from app.prompts.system_prompt import SYSTEM_PROMPT
from app.prompts.refactor_prompt import REFACTOR_PROMPT
from app.prompts.create_prompt import CREATE_PROMPT


class PromptService:
    """
    Builds structured prompts for resume generation/refactoring.
    """

    def build_prompt(self, mode: str, context: Dict[str, Any]) -> str:
        """
        Build final prompt based on mode and context.
        """

        if mode == "refactor":
            mode_prompt = REFACTOR_PROMPT
        elif mode == "create":
            mode_prompt = CREATE_PROMPT
        else:
            raise ValueError(f"Invalid prompt mode: {mode}")

        context_block = self._build_context_block(context)

        final_prompt = f"""
{mode_prompt}

==========================
CONTEXT
==========================
{context_block}

==========================
FINAL INSTRUCTIONS
==========================
Generate the final resume now.
"""

        return final_prompt.strip()

    def _build_context_block(self, context: Dict[str, Any]) -> str:
        """
        Formats dynamic context injected into the prompt.
        """

        return f"""
EXPERIENCE LEVEL:
{context.get("experience_level", "Not Provided")}

ROLE TYPE:
{context.get("role_type", "Not Provided")}

INDUSTRY:
{context.get("industry", "Not Provided")}

JOB DESCRIPTION:
{context.get("job_description", "")}

EXISTING RESUME CONTENT:
{context.get("resume_text", "")}

CANDIDATE DETAILS:
{context.get("candidate_data", "")}
""".strip()

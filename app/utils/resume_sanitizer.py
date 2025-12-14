import re

class ResumeSanitizer:
    """
    Cleans and normalizes LLM resume output.
    """

    @staticmethod
    def sanitize(text: str) -> str:
        # Remove markdown code blocks
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

        # Remove markdown headers and formatting
        text = re.sub(r"#+\s*", "", text)
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)

        # Remove bullets like ●
        text = text.replace("●", "-")

        # Remove commentary lines
        text = re.sub(r"This resume.*", "", text, flags=re.IGNORECASE)

        # Remove placeholder fields
        text = re.sub(r"\[.*?\]", "", text)

        # Fix broken words
        text = text.replace("AIpowered", "AI-powered")
        text = text.replace("FastAPIbased", "FastAPI-based")
        text = text.replace("authenticationready", "authentication-ready")

        # Normalize spacing
        lines = [line.strip() for line in text.split("\n")]
        clean_lines = [line for line in lines if line]

        return "\n".join(clean_lines)

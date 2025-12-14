from openai import AsyncOpenAI
from app.core.config import settings
from app.prompts.system_prompt import SYSTEM_PROMPT


class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    async def generate_resume(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1800,
            extra_headers={
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Resume AI Builder"
            }
        )

        return response.choices[0].message.content.strip()

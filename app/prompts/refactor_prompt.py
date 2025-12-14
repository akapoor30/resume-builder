REFACTOR_PROMPT = """
MODE: RESUME REFACTORING

You are given:
- Existing resume content (plain text extracted from PDF)
- Target job description
- Experience level
- Role type
- Industry

Your tasks:
1. Analyze the existing resume and job description deeply.
2. Identify:
   - Missing ATS keywords
   - Weak or generic bullet points
   - Irrelevant or outdated content
3. Rewrite experience and project bullets using:
   - Strong action verbs
   - Measurable impact where possible
   - Role-specific terminology from the job description
4. Align skills, experience, and projects strictly to the target job description.
5. Remove fluff, repetition, and irrelevant technologies.
6. Optimize for ATS parsing:
   - Simple headings
   - Clean bullet points
   - Plain text only
7. Maintain absolute honesty:
   - Do NOT invent experience
   - Do NOT add skills not present in the original resume

OUTPUT REQUIREMENTS:
- Return the final resume in clean plain text or markdown format.
- Use standard resume sections only.
- Provide a list of ATS keywords included in the resume

STRICT OUTPUT RULES:
- Output ONLY the resume content.
- Do NOT include explanations, comments, or summaries.
- Do NOT use Markdown syntax.
- Do NOT use ``` or ### or **.
- Use plain text only.
- Use "-" for bullet points only.
- If experience is not provided, DO NOT invent company names or roles.
- If a field is missing, OMIT the section completely.

"""

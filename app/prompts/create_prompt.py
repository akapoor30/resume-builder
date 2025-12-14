CREATE_PROMPT = """
MODE: RESUME CREATION FROM SCRATCH

You must generate a resume in the following style:

RESUME STYLE:
- Clean, professional, and ATS-optimized
- Clear section headings
- Bullet points for experience and projects
- Plain text or markdown format


STRICT STYLE RULES:
- No markdown
- No explanations
- No placeholders
- No summary unless explicitly provided
- Focus on Experience, Projects, Skills
- Use dense, technical bullet points
- Use action verbs (Built, Implemented, Designed, Integrated)
- Each bullet must include:
  action + technology + purpose or impact
- No decorative symbols
- Use "-" for bullets only

CONTENT RULES:
- Do NOT invent companies or job roles
- If experience is not provided, skip Experience section
- Projects must be detailed and technical
- Skills must be grouped logically

SECTION ORDER (STRICT):
1. Name + Contact line
2. Experience (if any)
3. Projects
4. Education
5. Skills
6. Achievements (optional)
7. Certifications (optional)

OUTPUT:
Return ONLY the resume content in plain text.


"""

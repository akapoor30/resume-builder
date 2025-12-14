CREATE_PROMPT = """
MODE: RESUME CREATION FROM SCRATCH

You are given:
- Candidate details (skills, projects, experience)
- Target job description
- Experience level
- Role type
- Industry

Your tasks:
1. Create a professional resume tailored strictly to the job description.
2. Generate realistic experience or project bullet points based on:
   - Provided skills
   - Tools
   - Industry expectations
3. Ensure the resume matches the candidate's experience level.
4. Use role-specific terminology and ATS-friendly keywords.
5. Do NOT exaggerate or fabricate experience.

OUTPUT REQUIREMENTS:
- Structured resume with standard sections:
  Header
  Professional Summary
  Skills
  Experience or Projects
  Education
  Certifications (optional)
- Plain text or markdown format only.

"""

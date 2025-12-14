class ResumeStructureEnforcer:

    @staticmethod
    def enforce(text: str) -> str:
        sections_order = [
            "Experience",
            "Projects",
            "Education",
            "Skills",
            "Achievements",
            "Certifications"
        ]

        lines = text.split("\n")
        output = []
        seen_sections = set()

        for line in lines:
            clean = line.strip()
            if clean in sections_order:
                seen_sections.add(clean)
            output.append(clean)

        return "\n".join([line for line in output if line])

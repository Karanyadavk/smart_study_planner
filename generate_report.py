from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def build_pdf(output_path: str = "docs/smart_study_planner_report.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=20,
    )
    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=8,
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        spaceAfter=8,
    )

    story.append(Paragraph("Smart Study Planner", title_style))
    story.append(Paragraph("Project Report", heading_style))
    story.append(Paragraph("This project is designed to help students manage academic subjects, tasks, and study sessions. It includes a modular Python architecture, persistent data storage, and a command-line interface for everyday use.", body_style))
    story.append(Paragraph("Objectives", heading_style))
    story.append(Paragraph("- Manage multiple subjects<br/>- Organize tasks with due dates and priorities<br/>- Track study time and notes<br/>- Generate weekly performance summaries", body_style))
    story.append(Paragraph("Functional Requirements", heading_style))
    story.append(Paragraph("- Add subject records<br/>- Add tasks with priority and deadlines<br/>- Log study sessions<br/>- Review subject-level and weekly summaries", body_style))
    story.append(Paragraph("Non-Functional Requirements", heading_style))
    story.append(Paragraph("- Performance: responsive for small student datasets<br/>- Usability: clear CLI interaction<br/>- Reliability: validation and safe storage<br/>- Maintainability: modular structure and documentation", body_style))
    story.append(Paragraph("Implementation Summary", heading_style))
    story.append(Paragraph("The application uses Python dataclasses to model subjects, tasks, and sessions, while JSON storage provides persistent local data management. Unit tests validate the planner logic and the CLI remains simple for educational deployment.", body_style))

    doc.build(story)
    print(f"PDF report generated at {output_path}")


if __name__ == "__main__":
    build_pdf()

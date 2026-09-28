from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class StudentTask:
    task_id: int
    subject: str
    title: str
    priority: str
    due_date: str
    completed: bool = False


@dataclass
class StudySession:
    session_id: int
    subject: str
    minutes: int
    notes: str
    session_date: str = field(default_factory=lambda: str(date.today()))


@dataclass
class StudyPlanner:
    subjects: List[str] = field(default_factory=list)
    tasks: List[StudentTask] = field(default_factory=list)
    sessions: List[StudySession] = field(default_factory=list)

    def add_subject(self, subject: str) -> None:
        subject_name = subject.strip()
        if not subject_name:
            raise ValueError("Subject name cannot be empty.")
        if subject_name not in self.subjects:
            self.subjects.append(subject_name)

    def add_task(self, task: StudentTask) -> None:
        if not task.title.strip():
            raise ValueError("Task title cannot be empty.")
        self.tasks.append(task)

    def add_session(self, session: StudySession) -> None:
        if session.minutes <= 0:
            raise ValueError("Study duration must be positive.")
        self.sessions.append(session)

    def get_subject_summary(self, subject: str) -> dict:
        total_minutes = sum(
            session.minutes for session in self.sessions if session.subject.lower() == subject.lower()
        )
        tasks = [task for task in self.tasks if task.subject.lower() == subject.lower()]
        completed = sum(1 for task in tasks if task.completed)
        return {
            "subject": subject,
            "total_minutes": total_minutes,
            "total_tasks": len(tasks),
            "completed_tasks": completed,
        }

    def weekly_summary(self) -> dict:
        total_minutes = sum(session.minutes for session in self.sessions)
        by_subject = {}
        for subject in self.subjects:
            by_subject[subject] = self.get_subject_summary(subject)["total_minutes"]
        return {
            "total_minutes": total_minutes,
            "subjects": by_subject,
            "tasks": len(self.tasks),
        }

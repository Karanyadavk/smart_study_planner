from __future__ import annotations

from study_planner.analytics import Analytics
from study_planner.models import StudyPlanner, StudentTask, StudySession
from study_planner.storage import StorageManager
from study_planner.utils import validate_date


def print_menu():
    print("\n=== Smart Study Planner ===")
    print("1. Add subject")
    print("2. Add task")
    print("3. Log study session")
    print("4. View subject summaries")
    print("5. View weekly summary")
    print("6. Exit")


def load_planner() -> StudyPlanner:
    manager = StorageManager()
    data = manager.load()
    planner = StudyPlanner()
    planner.subjects = data.get("subjects", [])
    planner.tasks = [
        StudentTask(
            task_id=task["task_id"],
            subject=task["subject"],
            title=task["title"],
            priority=task["priority"],
            due_date=task["due_date"],
            completed=task.get("completed", False),
        )
        for task in data.get("tasks", [])
    ]
    planner.sessions = [
        StudySession(
            session_id=session["session_id"],
            subject=session["subject"],
            minutes=session["minutes"],
            notes=session["notes"],
            session_date=session.get("session_date", "2026-01-01"),
        )
        for session in data.get("sessions", [])
    ]
    return planner


def save_planner(planner: StudyPlanner) -> None:
    StorageManager().save(planner)


def add_subject(planner: StudyPlanner) -> None:
    name = input("Enter subject name: ").strip()
    planner.add_subject(name)
    save_planner(planner)
    print(f"Subject '{name}' added.")


def add_task(planner: StudyPlanner) -> None:
    subject = input("Enter subject: ").strip()
    title = input("Enter task title: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().title()
    due_date = validate_date(input("Enter due date (YYYY-MM-DD): ").strip())
    task = StudentTask(
        task_id=len(planner.tasks) + 1,
        subject=subject,
        title=title,
        priority=priority,
        due_date=due_date,
    )
    planner.add_task(task)
    save_planner(planner)
    print(f"Task '{title}' added.")


def log_session(planner: StudyPlanner) -> None:
    subject = input("Enter subject: ").strip()
    minutes = int(input("Enter minutes studied: ").strip())
    notes = input("Add brief notes: ").strip()
    session = StudySession(
        session_id=len(planner.sessions) + 1,
        subject=subject,
        minutes=minutes,
        notes=notes,
    )
    planner.add_session(session)
    save_planner(planner)
    print(f"Study session logged for {subject}.")


def view_subject_summaries(planner: StudyPlanner) -> None:
    if not planner.subjects:
        print("No subjects available yet.")
        return
    for subject in planner.subjects:
        summary = planner.get_subject_summary(subject)
        print(
            f"{subject}: {summary['total_minutes']} minutes, "
            f"{summary['completed_tasks']}/{summary['total_tasks']} tasks completed"
        )


def view_weekly_summary(planner: StudyPlanner) -> None:
    print(Analytics.summarize(planner))


def main():
    planner = load_planner()
    while True:
        try:
            print_menu()
            choice = input("Select an option: ").strip()
        except EOFError:
            print("\nInput stream closed. Exiting gracefully.")
            break

        if choice == "1":
            add_subject(planner)
        elif choice == "2":
            add_task(planner)
        elif choice == "3":
            log_session(planner)
        elif choice == "4":
            view_subject_summaries(planner)
        elif choice == "5":
            view_weekly_summary(planner)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

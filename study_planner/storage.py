import json
from pathlib import Path


class StorageManager:
    def __init__(self, file_path: str = "data/study_data.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.file_path.exists():
            return {"subjects": [], "tasks": [], "sessions": []}
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {"subjects": [], "tasks": [], "sessions": []}

    def save(self, planner) -> None:
        payload = {
            "subjects": planner.subjects,
            "tasks": [
                {
                    "task_id": task.task_id,
                    "subject": task.subject,
                    "title": task.title,
                    "priority": task.priority,
                    "due_date": task.due_date,
                    "completed": task.completed,
                }
                for task in planner.tasks
            ],
            "sessions": [
                {
                    "session_id": session.session_id,
                    "subject": session.subject,
                    "minutes": session.minutes,
                    "notes": session.notes,
                    "session_date": session.session_date,
                }
                for session in planner.sessions
            ],
        }
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2)

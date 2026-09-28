# Design Diagrams

## Use Case Diagram

- Student can add a subject.
- Student can add a task.
- Student can log a study session.
- Student can view subject summary.
- Student can view weekly summary.

## Workflow

1. Start the application.
2. Select a menu option.
3. Enter subject/task/session details.
4. Save the data to storage.
5. Display summary or confirmation.

## Sequence Diagram

Student -> CLI: choose menu option
CLI -> Planner: create or update records
Planner -> Storage: save data
Storage -> JSON file: persist records
CLI -> Student: display confirmation/output

## Class Diagram

StudyPlanner
- subjects: list
- tasks: list
- sessions: list
- add_subject()
- add_task()
- add_session()
- get_subject_summary()
- weekly_summary()

StudentTask
- task_id
- subject
- title
- priority
- due_date
- completed

StudySession
- session_id
- subject
- minutes
- notes
- session_date

StorageManager
- load()
- save(planner)

Analytics
- summarize(planner)

# Smart Study Planner

A Python-based academic productivity tool designed for students to manage subjects, schedule study tasks, track study sessions, and generate weekly performance insights.

## Overview

The Smart Study Planner helps learners stay organized by combining subject management, task planning, and effort tracking in one system. It is useful for students who want to avoid last-minute preparation and monitor how much time they invest in each subject.

## Features

- Manage multiple academic subjects
- Add and organize study tasks by priority and due date
- Log study sessions with duration and notes
- Track weekly study time by subject
- Generate a compact performance summary
- Store data locally in JSON for easy persistence
- Use a simple command-line interface for quick interaction

## Tech Stack

- Python 3.10+
- Standard library modules only
- unittest for validation testing

## Folder Structure

```text
smart-study-planner/
├── app.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── architecture.md
│   └── diagrams.md
├── study_planner/
│   ├── __init__.py
│   ├── analytics.py
│   ├── cli.py
│   ├── models.py
│   ├── planner.py
│   ├── storage.py
│   └── utils.py
├── tests/
│   └── test_study_planner.py
└── data/
    └── study_data.json
```

## Installation

1. Clone or download the project.
2. Open a terminal in the project root.
3. Create a virtual environment if needed.
4. Install dependencies:

```bash
python -m venv .venv
. .venv/bin/activate    # Linux/macOS
# or
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The CLI menu allows you to:

- Add subjects
- Add tasks
- Log study sessions
- View subject summaries
- View weekly summary
- Exit the application

## Testing

Run the automated tests with:

```bash
python -m unittest discover -s tests -v
```

## Sample Workflow

1. Add subjects such as Data Structures and Operating Systems.
2. Add tasks and due dates for each subject.
3. Log study sessions with duration and short notes.
4. Review the weekly summary for performance and balance.

## Screenshots

This project is designed as a command-line application. Screenshots can be captured by running the app in a terminal and saving the output.

## Future Enhancements

- Add calendar-based scheduling
- Add CSV export for study reports
- Add graphical dashboard using a web frontend
- Add user authentication and cloud sync

## License

This project is intended for academic submission and learning purposes.

# Smart Study Planner

## 1. Introduction
The Smart Study Planner is a Python-based academic management system designed to help students plan their study tasks, monitor weekly workload, and track performance across subjects. The project addresses the common challenge of balancing multiple subjects and deadlines without a dedicated organization tool.

## 2. Problem Statement
Students often struggle to keep track of assignment deadlines, revision schedules, and study time across several subjects. This leads to poor time management, increased stress, and reduced academic performance. A simple planner can improve coordination and productivity.

## 3. Functional Requirements
- Add and manage academic subjects.
- Create study tasks with priorities and due dates.
- Log study sessions with time spent and notes.
- View subject-wise study summaries.
- View a weekly summary of total study minutes.

## 4. Non-Functional Requirements
- Performance: quick response for small data loads.
- Usability: simple command-line navigation.
- Reliability: validation of inputs and safe storage operations.
- Maintainability: modular package structure for future changes.
- Security: local JSON storage with no external data exposure.

## 5. System Architecture
The system follows a three-layer structure:
- Presentation layer: CLI menu interface
- Logic layer: planner and analytics logic
- Data layer: JSON storage manager

## 6. Design Diagrams
Use case, workflow, sequence, and class diagrams are documented in the docs folder. They describe the interaction flow between the student, CLI, planner logic, and persistent storage.

## 7. Design Decisions and Rationale
- Python dataclasses simplify object modeling.
- JSON storage fits the project scope and keeps it portable.
- A command-line interface is appropriate for a beginner-friendly academic project.

## 8. Implementation Details
The implementation is split into modules such as models, storage, analytics, cli, and utils. Each module handles a specific responsibility, which improves maintainability and readability.

## 9. Testing Approach
Unit tests validate subject creation, task creation, session logging, summary retrieval, and weekly summaries. The project uses Python’s built-in unittest framework.

## 10. Challenges Faced
- Designing a simple but modular architecture.
- Managing state persistence cleanly.
- Ensuring invalid input does not break the program.

## 11. Learnings and Key Takeaways
This project reinforced core software engineering practices such as modularization, validation, and testing. It also demonstrated how data modeling and storage can be aligned with real-world academic needs.

## 12. Future Enhancements
- Add graphical dashboard.
- Support CSV export.
- Add recurring tasks and reminders.
- Introduce user authentication for multi-user support.

## 13. References
- Python Documentation
- unittest Documentation
- Academic project requirement guidelines from the course brief

# System Architecture

## Overview

The Smart Study Planner uses a modular, layered design. The application is centered around a planner model that holds the core data for subjects, tasks, and study sessions.

## Layers

1. Presentation Layer
   - CLI interface handles user interaction.
   - Displays menu options and summary output.

2. Application Logic Layer
   - The planner logic manages creation and retrieval of academic records.
   - Analytics provides summaries and progress insights.

3. Data Layer
   - StorageManager reads and writes JSON files.
   - Data persists in `data/study_data.json`.

## Flow

User -> CLI -> Planner model -> StorageManager -> JSON file  -> Analytics -> Summary output

## Design Decisions

- Python dataclasses are used for clean data modeling.
- JSON persistence keeps the project simple and portable.
- Modular file organization allows easier future extension to a GUI or web app.

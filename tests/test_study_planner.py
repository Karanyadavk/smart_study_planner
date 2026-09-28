import unittest

from study_planner.models import StudyPlanner, StudentTask, StudySession


class TestStudyPlanner(unittest.TestCase):
    def test_add_subject(self):
        planner = StudyPlanner()
        planner.add_subject("Math")
        self.assertIn("Math", planner.subjects)

    def test_add_task(self):
        planner = StudyPlanner()
        task = StudentTask(1, "Math", "Solve algebra worksheet", "High", "2026-09-30")
        planner.add_task(task)
        self.assertEqual(len(planner.tasks), 1)

    def test_add_session(self):
        planner = StudyPlanner()
        session = StudySession(1, "Math", 45, "Revision and practice")
        planner.add_session(session)
        self.assertEqual(planner.sessions[0].minutes, 45)

    def test_get_subject_summary(self):
        planner = StudyPlanner(subjects=["Math"])
        planner.add_session(StudySession(1, "Math", 60, "Chapter review"))
        planner.add_task(StudentTask(1, "Math", "Practice set", "Medium", "2026-09-29", True))
        summary = planner.get_subject_summary("Math")
        self.assertEqual(summary["total_minutes"], 60)
        self.assertEqual(summary["completed_tasks"], 1)

    def test_weekly_summary(self):
        planner = StudyPlanner(subjects=["Math", "Science"])
        planner.add_session(StudySession(1, "Math", 30, "Algebra"))
        planner.add_session(StudySession(2, "Science", 50, "Physics"))
        summary = planner.weekly_summary()
        self.assertEqual(summary["total_minutes"], 80)
        self.assertIn("Math", summary["subjects"])


if __name__ == "__main__":
    unittest.main()

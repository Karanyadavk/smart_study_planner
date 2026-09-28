class Analytics:
    @staticmethod
    def summarize(planner):
        summary = planner.weekly_summary()
        if not summary["subjects"]:
            return "No study data yet. Add a subject and log a session."

        lines = ["Weekly Study Summary", "--------------------"]
        for subject, minutes in summary["subjects"].items():
            lines.append(f"{subject}: {minutes} minutes")
        lines.append(f"Total study time: {summary['total_minutes']} minutes")
        lines.append(f"Tracked tasks: {summary['tasks']}")
        return "\n".join(lines)

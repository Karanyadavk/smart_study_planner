from datetime import datetime


def validate_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError as exc:
        raise ValueError("Date must be in YYYY-MM-DD format.") from exc

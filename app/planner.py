from pathlib import Path
from datetime import datetime
import yaml

DATA = Path(__file__).parent.parent / "data"

DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


def get_plan(day):

    with open(DATA / f"{day}.yaml") as f:
        return yaml.safe_load(f)


def get_today_plan():

    today = DAYS[datetime.now().weekday()]

    return get_plan(today)


def get_tomorrow_plan():

    tomorrow = DAYS[(datetime.now().weekday() + 1) % 7]

    return get_plan(tomorrow)
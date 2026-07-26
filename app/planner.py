from datetime import datetime
import yaml

DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]

def get_today_plan():

    today = DAYS[datetime.utcnow().weekday()]

    with open(f"data/{today}.yaml") as f:
        return yaml.safe_load(f)

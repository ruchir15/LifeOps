import os

from app.planner import get_tomorrow_plan
from app.formatter import format_meal
from app.telegram import send

plan = get_tomorrow_plan()

send(
    os.environ["BOT_TOKEN"],
    os.environ["CHAT_ID_SAKSHI"],
    format_meal(plan),
)
import os

from app.planner import get_today_plan
from app.formatter import format_workout
from app.telegram import send

plan = get_today_plan()

send(
    os.environ["BOT_TOKEN"],
    os.environ["CHAT_ID_RUCHIR"],
    format_workout(plan),
)
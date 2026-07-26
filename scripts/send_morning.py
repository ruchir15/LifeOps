import os

from app.planner import get_today_plan
from app.formatter import format_message
from app.telegram import send

plan = get_today_plan()

message = format_message(plan)

send(
    os.environ["CHAT_ID_RUCHIR"],
    message,
)

print("Morning notification sent.")

import os
import requests

token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["CHAT_ID_RUCHIR"]

message = """
🏃 Good Morning!

LifeOps is working successfully.

Have a great day!
"""

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": chat_id,
        "text": message,
    },
).raise_for_status()

print("Message sent successfully.")

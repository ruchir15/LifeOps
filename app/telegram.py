import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

def send(chat_id, message):

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
        },
    ).raise_for_status()

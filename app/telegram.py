import requests


def send(bot_token: str, chat_id: str, message: str):

    response = requests.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        },
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()
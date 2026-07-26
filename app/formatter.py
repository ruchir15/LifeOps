def format_message(plan):

    workout = "\n".join(
        f"• {x}" for x in plan["workout"]
    )

    breakfast = ", ".join(plan["breakfast"])

    return f"""
🏃 {plan['day']}

🥣 Breakfast
{breakfast}

🏋 Workout
{workout}

💧 Water
{plan['water_goal']}

🚶 Steps
{plan['steps']}
"""

def bullets(items):
    return "\n".join(f"• {x}" for x in items)


def format_workout(plan):

    return f"""
🏃 *{plan['day']}*

🥣 Breakfast

{bullets(plan['breakfast'])}

🏋️ Workout

{bullets(plan['workout'])}

💧 Water
{plan['water_goal']}

🚶 Steps
{plan['steps']}
"""

def format_meal(plan):

    return f"""
🍽️ *Tomorrow's Meal Plan*

🥣 Breakfast

{bullets(plan['breakfast'])}

🍛 Lunch

{bullets(plan['lunch'])}

☕ Evening Snack

{bullets(plan['evening_snack'])}

🍽️ Dinner

{bullets(plan['dinner'])}

❤️ Please prepare these meals for tomorrow.
"""

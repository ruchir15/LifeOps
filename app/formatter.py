def bullet_list(items):
    return "\n".join(f"• {item}" for item in items)


def format_message(plan):
    return f"""
🏃 *{plan['day']}*

🥣 *Breakfast*
{', '.join(plan['breakfast'])}

🍎 *Morning Snack*
{', '.join(plan['morning_snack'])}

🍛 *Lunch*
{', '.join(plan['lunch'])}

☕ *Evening Snack*
{', '.join(plan['evening_snack'])}

🍽️ *Dinner*
{', '.join(plan['dinner'])}

🏋️ *Workout*
{bullet_list(plan['workout'])}

💧 *Water Goal*
{plan['water_goal']}

🚶 *Steps*
{plan['steps']}

😴 *Sleep*
{plan['sleep_goal']}

💪 *Today's Motivation*
_{plan['motivation']}_
"""

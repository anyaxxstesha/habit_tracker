import requests

from config import settings


def tg_notification(msg, chat_id):
    """Send a notification to the given chat"""
    params = {
        'chat_id': chat_id,
        'text': msg
    }
    requests.post(
        url=settings.TELEGRAM_BOT_URL,
        json=params
    )


def start_notification(habits):
    """Send notifications by the given habits"""
    for habit in habits:
        reward = None
        related_habit = None
        if habit.related_habit:
            related_habit = (
                f'Привычку "{habit.related_habit.action}" необходимо выполнить в {habit.related_habit.place}'
                f' в {habit.related_habit.perform_at}')
        else:
            reward = habit.reward

        msg = (f'Пора выполнить привычку!\n'
               f'Привычка: "{habit.related_habit.action}"\n'
               f'Место выполнения: {habit.related_habit.place}\n'
               f'Награда: {related_habit or reward}')
        tg_notification(msg, habit.user.telegram_chat_id)

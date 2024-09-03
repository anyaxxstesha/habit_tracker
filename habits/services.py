import requests

from config import settings


def tg_notification(msg, chat_id):
    """Send a notification to the given chat"""
    params = {
        'chat_id': chat_id,
        'text': msg
    }
    f = requests.post(
        url=settings.TELEGRAM_BOT_URL,
        json=params
    )
    print(f.json())


def start_notification(habits):
    """Send notifications by the given habits"""
    for habit in habits:
        reward = None
        associated_habit = None
        if habit.associated_habit:
            associated_habit = (
                f'Привычку "{habit.associated_habit.action}" необходимо выполнить в {habit.associated_habit.place}'
                f' в {habit.associated_habit.perform_at}')
        else:
            reward = habit.reward

        msg = (f'Пора выполнить привычку!\n'
               f'Привычка: "{habit.action}"\n'
               f'Место выполнения: {habit.place}\n'
               f'Награда: {associated_habit or reward}')
        tg_notification(msg, habit.owner.telegram_chat_id)

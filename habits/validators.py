from datetime import timedelta

from rest_framework.serializers import ValidationError


def pleasant_habit_or_reward(value):
    """Проверяет, что в модели заполнено либо поле associated_habit, либо reward"""
    reward = value.get('reward')
    associated_habit = value.get('associated_habit')
    if bool(reward) + bool(associated_habit) != 1:
        raise ValidationError("В привычке должны указываться либо связанная привычка, либо вознаграждение")


def habit_time_check(habit_time):
    """Проверяет, что в модели habit_time не больше 120 секунд"""
    if habit_time > timedelta(minutes=2):
        raise ValidationError("Время выполнения привычки не должно быть больше 120 секунд")

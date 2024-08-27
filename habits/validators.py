from datetime import timedelta

from rest_framework.serializers import ValidationError


def pleasant_habit_or_reward(value):
    """
    Проверяет, что в модели полезной привычки заполнено либо поле associated_habit, либо reward.
    В модели приятной привычки не могут быть заполнены поля associated_habit и reward
    """
    reward = value.get('reward')
    associated_habit = value.get('associated_habit')
    is_pleasant = value.get('is_pleasant')
    fields_presence = bool(reward) + bool(associated_habit)
    if is_pleasant and fields_presence != 0:
        raise ValidationError("В приятной привычке не должны быть заполнены поля associated_habit и reward")
    if not is_pleasant and fields_presence != 1:
        raise ValidationError("В полезной привычке должны быть заполнены либо поле associated_habit, либо поле reward")


def habit_time_check(habit_time):
    """Проверяет, что в модели привычки поле habit_time не больше 120 секунд"""
    if habit_time > timedelta(minutes=2):
        raise ValidationError("Время выполнения привычки не должно быть больше 120 секунд")


def frequency_check(frequency):
    """Проверяет, что в модели привычки поле frequency не больше 7 дней"""
    if frequency > timedelta(days=7):
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")

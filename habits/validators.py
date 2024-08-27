from rest_framework.serializers import ValidationError


def pleasant_habit_or_reward(value):
    reward = value.get('reward')
    associated_habit = value.get('associated_habit')
    if bool(reward) + bool(associated_habit) != 1:
        raise ValidationError("В привычке должны указываться либо связанная привычка, либо вознаграждение")

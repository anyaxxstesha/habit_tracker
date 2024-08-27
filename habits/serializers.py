from rest_framework import serializers

from habits.models import Habit
from habits.validators import pleasant_habit_or_reward, habit_time_check


class HabitSerializer(serializers.ModelSerializer):
    habit_time = serializers.DurationField(validators=[habit_time_check])
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            pleasant_habit_or_reward,
        ]

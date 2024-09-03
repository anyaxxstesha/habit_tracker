from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_time_check, frequency_check, PleasantHabitOrReward


class HabitSerializer(serializers.ModelSerializer):
    habit_time = serializers.DurationField(validators=[habit_time_check])
    frequency = serializers.DurationField(validators=[frequency_check])
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            PleasantHabitOrReward(),
        ]

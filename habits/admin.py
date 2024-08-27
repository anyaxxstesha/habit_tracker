from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'performance_time', 'is_pleasant', 'associated_habit', 'frequency', 'is_public')
    list_filter = ('is_pleasant', 'owner')
    search_fields = ('owner',)

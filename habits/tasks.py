from celery import shared_task
from django.db.models import F
from django.utils import timezone

from habits.models import Habit
from habits.services import start_notification


@shared_task
def send_notification_celery():
    """Отправляет напоминание в Telegram для выполнения привычки"""
    now = timezone.now()
    queryset = Habit.objects.filter(perform_at__lt=now).prefetch_related('owner', 'associated_habit')
    start_notification(habits=queryset)
    queryset.update(next_perform_at=F('next_perform_at') + F('frequency'))

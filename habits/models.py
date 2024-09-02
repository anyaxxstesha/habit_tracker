from datetime import timedelta

from django.db import models
from django.utils import timezone

from config import settings


class Habit(models.Model):
    """
    Model for habit
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                              verbose_name='Создатель',
                              related_name='course', help_text='Укажите создателя привычки')
    place = models.TextField(verbose_name='Место для выполнения привычки',
                             help_text='Укажите место для выполнения привычки')
    perform_at = models.TimeField(verbose_name='Время, когда необходимо выполнять привычку',
                                  help_text='Укажите время, когда необходимо выполнять привычку')
    action = models.TextField(verbose_name='Действие, которое представляет собой привычка',
                              help_text='Укажите действие, которое представляет собой привычка')
    is_pleasant = models.BooleanField(blank=True, null=True, default=False, verbose_name='Флаг приятной привычки',
                                      help_text='Укажите, является ли привычка приятной')
    associated_habit = models.ForeignKey('Habit', blank=True, null=True, verbose_name='Связанная привычка',
                                         help_text='Укажите связанную привычку', related_name='useful_habit',
                                         on_delete=models.SET_NULL)
    frequency = models.DurationField(default=timedelta(days=1), verbose_name='Периодичность выполнения привычки в днях',
                                     help_text='Укажите периодичность выполнения привычки в днях')
    reward = models.TextField(verbose_name='Вознаграждение за выполнение привычки',
                              help_text='Укажите вознаграждение за выполнение привычки', blank=True, null=True)
    habit_time = models.DurationField(default=timedelta(minutes=1),
                                      verbose_name='Время в минутах, которое предположительно потратит пользователь на выполнение привычки',
                                      help_text='Укажите время в минутах, которое предположительно потратит пользователь на выполнение привычки')
    is_public = models.BooleanField(blank=True, null=True, default=False, verbose_name='Флаг публичной привычки',
                                    help_text='Укажите, является ли привычка публичной')
    next_perform_at = models.DateTimeField(blank=True, null=True,
                                           verbose_name='Следующая дата и время выполнения привычки',
                                           help_text='Укажите следующую дату и время выполнения привычки')

    def set_next_perform_at(self):
        now = timezone.now()
        if self.next_perform_at is None or self.next_perform_at < now.date():
            if self.perform_at <= now.time():
                day = (now.today() + timedelta(days=1)).day
            else:
                day = now.today().day

            self.next_perform_at = timezone.datetime(year=now.year, month=now.month, day=day, hour=self.perform_at.hour,
                                                     minute=self.perform_at.minute,
                                                     tzinfo=timezone.get_current_timezone())

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.set_next_perform_at()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

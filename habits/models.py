from datetime import timedelta

from django.db import models

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
    performance_time = models.TimeField(verbose_name='Время выполнения привычки',
                                        help_text='Укажите время выполнения привычки')
    action = models.TextField(verbose_name='Действие, которое представляет собой привычка',
                              help_text='Укажите действие, которое представляет собой привычка')
    is_pleasant = models.BooleanField(blank=True, null=True, default=False, verbose_name='Флаг приятной привычки',
                                      help_text='Укажите, является ли привычка приятной')
    associated_habit = models.ForeignKey('Habit', blank=True, null=True, verbose_name='Связанная привычка',
                                         help_text='Укажите связанную привычку', related_name='useful_habit',
                                         on_delete=models.SET_NULL)
    frequency = models.DurationField(default=timedelta(days=1), verbose_name='Время на выполнение привычки',
                                     help_text='Укажите время на выполнение привычки')
    is_public = models.BooleanField(blank=True, null=True, default=False, verbose_name='Флаг публичной привычки',
                                      help_text='Укажите, является ли привычка публичной')

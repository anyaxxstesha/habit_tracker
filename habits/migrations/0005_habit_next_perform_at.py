# Generated by Django 5.1 on 2024-09-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_rename_performance_time_habit_perform_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='next_perform_at',
            field=models.DateTimeField(blank=True, help_text='Укажите следующую дату и время выполнения привычки', null=True, verbose_name='Следующая дата и время выполнения привычки'),
        ),
    ]

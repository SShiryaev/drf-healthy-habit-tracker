from datetime import timedelta

from django.db import models

from users.models import User


class Habit(models.Model):
    """Модель привычки"""

    PERIODICITY_CHOICES = [
        ('DAILY', 'ежедневно'),
        ('WEEKLY', 'еженедельно'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    place = models.CharField(
        max_length=200,
        verbose_name='место'
    )
    time = models.TimeField(
        verbose_name='время'
    )
    action = models.CharField(
        max_length=250,
        verbose_name='действие'
    )
    is_enjoyable = models.BooleanField(
        default=False,
        verbose_name='признак приятной привычки'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='связанная привычка'
    )
    periodicity = models.CharField(
        max_length=20,
        choices=PERIODICITY_CHOICES,
        default='DAILY',
        verbose_name='периодичность'
    )
    reward = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='вознаграждение'
    )
    duration = models.DurationField(
        default=timedelta(minutes=2),
        verbose_name='продолжительность выполнения'
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name='признак публичности'
    )

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

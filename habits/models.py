from datetime import timedelta

from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import User


class Habit(models.Model):
    """
    Модель привычки.
    Может быть связанна с собой с отношением один ко многим (O2M).
    """

    PERIODICITY_CHOICES = [
        (None, 'без периода'),
        (0, 'понедельник'),
        (1, 'вторник'),
        (2, 'среда'),
        (3, 'четверг'),
        (4, 'пятница'),
        (5, 'суббота'),
        (6, 'воскресенье'),
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
    periodicity = ArrayField(
        models.IntegerField(
            choices=PERIODICITY_CHOICES,
            blank=True,
            null=True,
            verbose_name='периодичность'
        ),
        size=8,
        blank=True,
        null=True,
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

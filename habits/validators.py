from datetime import timedelta

from rest_framework.serializers import ValidationError

from habits.models import Habit


class DetachmentFieldsValidator:
    """Валидация одновременного выбора связанной привычки и указания вознаграждения."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)
        reward = dict(value).get(self.field_2)

        if related_habit and reward:
            raise ValidationError(f'Fields {self.field_1} and {self.field_2} cannot be both True')


class DurationValidator:
    """Валидация на длительность выполнения привычки более двух минут."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        max_time = timedelta(minutes=2)

        if duration > max_time:
            raise ValidationError(f'{self.field} should not be more than two minutes')


class RelatedEnjoyableHabitValidator:
    """Валидация на связанную привычку только с флагом приятной привычки."""

    def __init__(self, field_1):
        self.field_1 = field_1

    def __call__(self, value):
        related_habit = dict(value).get(self.field_1)

        if related_habit:
            if not related_habit.is_enjoyable:
                raise ValidationError(f'{self.field_1} should be enjoyable')


class EnjoyableHabitValidator:
    """Валидация приятной привычки на вознаграждение или связанной привычки."""

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        reward = dict(value).get(self.field_1)
        related_habit = dict(value).get(self.field_2)
        is_enjoyable = dict(value).get(self.field_3)
        error_message = 'Enjoyable habit cannot have'

        if is_enjoyable:
            if reward:
                raise ValidationError(f'{error_message} {self.field_1}')
            elif related_habit:
                raise ValidationError(f'{error_message} {self.field_2}')


class PeriodicityValidator:
    """Валидация на выполнение привычки не реже, чем 1 раз в 7 дней."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)

        if periodicity not in Habit.PERIODICITY_CHOICES:
            raise ValidationError(f'{self.field} must be in {Habit.PERIODICITY_CHOICES}')

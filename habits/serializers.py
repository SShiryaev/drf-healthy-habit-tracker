from rest_framework import serializers

from habits import validators
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)
        validators = [
            validators.DetachmentFieldsValidator(field_1='related_habit', field_2='reward'),
            validators.DurationValidator(field='duration'),
            validators.RelatedEnjoyableHabitValidator(field_1='related_habit'),
            validators.EnjoyableHabitValidator(field_1='reward', field_2='related_habit', field_3='is_enjoyable'),
        ]

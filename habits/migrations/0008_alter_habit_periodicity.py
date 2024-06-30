# Generated by Django 5.0.6 on 2024-06-29 23:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(None, 'без периода'), (0, 'понедельник'), (1, 'вторник'), (2, 'среда'), (3, 'четверг'), (4, 'пятница'), (5, 'суббота'), (6, 'воскресенье')], null=True, verbose_name='периодичность'), blank=True, null=True, size=8, verbose_name='периодичность'),
        ),
    ]

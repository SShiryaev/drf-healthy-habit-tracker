# Generated by Django 5.0.6 on 2024-06-29 23:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('MONDAY', 'понедельник'), ('TUESDAY', 'вторник'), ('WEDNESDAY', 'среда'), ('THURSDAY', 'четверг'), ('FRIDAY', 'пятница'), ('SATURDAY', 'суббота'), ('SUNDAY', 'воскресенье')], max_length=20, null=True, verbose_name='периодичность'), blank=True, null=True, size=7),
        ),
    ]

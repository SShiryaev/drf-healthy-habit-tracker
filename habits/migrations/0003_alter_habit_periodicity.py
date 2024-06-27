# Generated by Django 5.0.6 on 2024-06-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(blank=True, choices=[(None, 'без периода'), ('DAILY', 'ежедневно'), ('ONCE_TWO_DAYS', 'раз в два дня'), ('ONCE_THREE_DAYS', 'раз в три дня'), ('ONCE_FOUR_DAYS', 'раз в четыре дня'), ('ONCE_FIVE_DAYS', 'раз в пять дней'), ('ONCE_SIX_DAYS', 'раз в шесть дней'), ('WEEKLY', 'еженедельно')], default='DAILY', max_length=20, null=True, verbose_name='периодичность'),
        ),
    ]
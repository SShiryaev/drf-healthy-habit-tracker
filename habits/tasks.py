import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_notification():
    time_now = datetime.datetime.now()
    weekday_now = time_now.weekday()
    habits = Habit.objects.all()

    for habit in habits:
        if weekday_now in habit.periodicity and \
                habit.time.hour == time_now.hour and \
                habit.time.minute == time_now.minute:
            tg_chat_id = habit.user.tg_chat_id
            message = f'Уведомление о привычке: {habit}'
            send_telegram_message(message, tg_chat_id)

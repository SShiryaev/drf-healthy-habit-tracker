from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.habit = Habit.objects.create(
            user=self.user,
            place='place',
            time='17:00:00',
            action='action',
            duration='00:00:30'
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse('habits:habit-create')
        data = {
            'place': 'тестовое место',
            'time': '18:00:00',
            'action': 'проводить тесты',
            "is_enjoyable": False,
            "periodicity": [5, 6],
            'reward': 'покрытие тестами 80%',
            'duration': '00:00:30',
            'is_public': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse('habits:habit-update', args=(self.habit.pk,))
        data = {
            'place': 'другое тестовое место',
            'duration': '00:00:35'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('place'), 'другое тестовое место')
        self.assertEqual(data.get('duration'), '00:00:35')

    def test_habit_destroy(self):
        url = reverse('habits:habit-delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse('habits:habit-list')
        response = self.client.get(url)
        data = response.json()
        sample = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "is_enjoyable": self.habit.is_enjoyable,
                    "periodicity": self.habit.periodicity,
                    "reward": self.habit.reward,
                    "duration": self.habit.duration,
                    "is_public": self.habit.is_public,
                    "user": self.habit.user.pk,
                    "related_habit": self.habit.related_habit
                },
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, sample)

    def test_habit_public_list(self):
        url = reverse('habits:habit-public-list')
        response = self.client.get(url)
        data = response.json()
        sample = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "is_enjoyable": self.habit.is_enjoyable,
                    "periodicity": self.habit.periodicity,
                    "reward": self.habit.reward,
                    "duration": self.habit.duration,
                    "is_public": True,
                    "user": self.habit.user.pk,
                    "related_habit": self.habit.related_habit
                },
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, sample)

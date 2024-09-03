from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            place="Дома",
            perform_at=timezone.now().time(),
            action="Сделать зарядку",
            is_pleasant=True,
            is_public=True,
            owner=self.user
        )

    def test_habit_retrieve(self):
        url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), self.habit.action
        )

    def test_habit_create(self):
        url = reverse("habits:habit_create")

        data = {
            "habit_time": "00:01:30",
            "place": "Дома",
            "perform_at": "09:00:00",
            "action": "Сделать зарядку",
            "is_pleasant": True,
            "frequency": "1 00:00:00",
            "is_public": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "place": "Habit updated"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("place"), "Habit updated"
        )

    def test_habit_delete(self):
        url = reverse("materials:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            Habit.objects.all().count(), data.get('count')
        )

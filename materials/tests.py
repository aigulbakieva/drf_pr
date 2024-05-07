from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com", password="123qwe", is_active=True)
        self.course = Course.objects.create(title="Базовый курс", owner=self.user)
        self.lesson = Lesson.objects.create(title='Вводный урок', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), self.lesson.title
        )

    def test_lesson_create(self):
        url = reverse("materials:lessons-create")
        data = {
            "title": "test",
            "owner": self.user.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_lesson_update(self):
        url = reverse("materials:lessons-update", args=(self.lesson.pk,))
        data = {
            "title": "test"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("title"), "test"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lessons-delete", args=(self.lesson.pk,))
        data = {
            "title": "test"
        }
        response = self.client.delete(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lessons-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "url": None,
                    "title": self.lesson.title,
                    "description": None,
                    "preview": None,
                    "course": None,
                    "owner": self.user.pk
                },
            ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com", password="123qwe", is_active=True)
        self.course = Course.objects.create(title="Базовый курс", owner=self.user)
        self.client.force_authenticate(user=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

    def test_subscription_create(self):
        url = reverse("materials:subscription-list")
        data = {
            "user": self.user.id,
            "course": self.course.id
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

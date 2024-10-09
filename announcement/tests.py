from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcement.models import Announcement, Feedback
from user.models import User


class AnnouncementTestCase(APITestCase):

    def setUp(self):
        """
        создаем бд
        """
        self.user = User.objects.create(
            email="py.te.2@mail.ru",
            password="Cxzaq12ws",
            first_name="Admin",
            last_name="IsAdmin",
            phone="89999990099",
            role="admin",
        )
        self.announcement = Announcement.objects.create(
            title="Самокат",
            price="5000",
            description="Самокат для детей",
            author=self.user,
            created_at="2024-10-07 18:02:10.528525+03",
        )
        self.client.force_authenticate(user=self.user)  # авторизовываемся

    def test_announcement_retrieve(self):
        """
        Проверяем получение объявления
        """
        url = reverse(
            "announcement:announcement_retrieve", args=(self.announcement.pk,)
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_announcement_create(self):
        """
        Проверяем создание объявления
        """
        url = reverse("announcement:announcement_create")
        data = {
            "title": "Самокат",
            "price": 5000,
            "description": "Самокат для взрослых",
            "author": self.user.pk,
            "created_at": "2024-10-08 18:17:19.100385+03",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Announcement.objects.count(), 2)

    def test_announcement_update(self):
        """
        Проверяем изменение объявления
        """
        url = reverse("announcement:announcement_update", args=(self.announcement.pk,))
        data = {"title": "Велосипед"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Велосипед")

    def test_announcement_destroy(self):
        """
        Проверяем удаление объявления
        """
        url = reverse("announcement:announcement_destroy", args=(self.announcement.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Announcement.objects.all().count(), 0)

    def test_announcement_list(self):
        """
        Проверяем получение списка объявлений
        """
        url = reverse("announcement:announcement_list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FeedbackTestCase(APITestCase):

    def setUp(self):
        """
        создаем бд
        """
        self.user = User.objects.create(
            email="py.te.2@mail.ru",
            password="Cxzaq12ws",
            first_name="Admin",
            last_name="IsAdmin",
            phone="89999990099",
            role="admin",
        )
        self.announcement = Announcement.objects.create(
            title="Самокат",
            price="5000",
            description="Самокат для детей",
            author=self.user,
            created_at="2024-10-07 18:02:10.528525+03",
        )
        self.feedback = Feedback.objects.create(
            text="Отличный самокат",
            author=self.user,
            ad=self.announcement,
            created_at="2024-10-08 18:17:19.100385+03",
        )
        self.client.force_authenticate(user=self.user)  # авторизовываемся

    def test_feedback_retrieve(self):
        """
        Проверяем получение отзыва
        """
        url = reverse("announcement:feedback_retrieve", args=(self.feedback.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_feedback_create(self):
        """
        Проверяем создание отзыва
        """
        url = reverse("announcement:feedback_create")
        data = {
            "text": "Отличный самокат",
            "ad": self.announcement.pk,
            "author": self.user.pk,
            "created_at": "2024-10-08 18:17:19.100385+03",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 2)

    def test_feedback_update(self):
        """
        Проверяем изменение отзыва
        """
        url = reverse("announcement:feedback_update", args=(self.feedback.pk,))
        data = {"text": "Отличный самокат для прогулок"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("text"), "Отличный самокат для прогулок")

    def test_feedback_destroy(self):
        """
        Проверяем удаление отзыва
        """
        url = reverse("announcement:feedback_destroy", args=(self.feedback.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feedback.objects.all().count(), 0)

    def test_feedback_list(self):
        """
        Проверяем получение списка отзывов
        """
        url = reverse("announcement:feedback_list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

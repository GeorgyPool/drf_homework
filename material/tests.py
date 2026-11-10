from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from material.models import Course, Lesson
from users.models import User


class TestLessons(APITestCase):

    def setUp(self):
        """Создания тестовых данных"""

        # создание тестового пользователя и тестового курса
        self.user_owner = User.objects.create(email="user_owner@example.com")
        self.other_user = User.objects.create(email="other_user@example.com")
        self.test_course = Course.objects.create(title="test", owner=self.user_owner)

        # создание тестового урока
        self.test_lesson = Lesson.objects.create(
            title="test 2", course=self.test_course, owner=self.user_owner
        )

    def test_create_lessons(self):
        self.client.force_authenticate(user=self.user_owner)
        data = {
            "title": "test",
            "course": self.test_course.pk,
        }
        response = self.client.post("/material/lesson/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("owner"), self.user_owner.pk)
        self.assertEqual(response.json().get("title"), "test")

    def test_read_list_lesson(self):
        self.client.force_authenticate(user=self.user_owner)
        response = self.client.get("/material/lesson/read/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["results"][0].get("owner"), self.user_owner.pk)
        self.assertEqual(response.json()["results"][0].get("title"), "test 2")

    def test_read_retrieve(self):
        self.client.force_authenticate(user=self.user_owner)
        response = self.client.get(
            f"/material/lesson/read/retrieve/{self.test_lesson.pk}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("title"), "test 2")
        self.assertEqual(response.json().get("owner"), self.user_owner.pk)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user_owner)
        data = {"title": "test_update"}
        response = self.client.patch(
            f"/material/lesson/update/{self.test_lesson.pk}/", data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("title"), "test_update")
        self.assertEqual(response.json().get("owner"), self.user_owner.pk)

    def test_bad_delete_lesson(self):
        self.client.force_authenticate(user=self.other_user)
        response = self.client.delete(f"/material/lesson/delete/{self.test_lesson.pk}/")
        self.assertEqual(response.json().get("detail"), "У вас недостаточно прав для выполнения данного действия.")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user_owner)
        response = self.client.delete(f"/material/lesson/delete/{self.test_lesson.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        lesson = Lesson.objects.filter(pk=self.test_lesson.pk).exists()
        self.assertEqual(lesson, False)

    def tearDown(self):
        User.objects.get(email=self.user_owner.email).delete()

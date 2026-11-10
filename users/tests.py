from django.template.defaultfilters import title
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from material.models import Course, Lesson
from users.models import Subscription, User


class TestSubscription(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create(email="test_user@example.com")
        self.test_second_user = User.objects.create(email="test_second_user")

        self.test_course = Course.objects.create(title="test_course")
        self.test_lesson = Lesson.objects.create(
            title="test_lesson", course=self.test_course
        )

        self.test_second_course = Course.objects.create(title="test_course_second")
        self.test_third_course = Course.objects.create(title="test_third_course")
        self.test_first_subscribe = Subscription.objects.create(
            user=self.test_user, course=self.test_second_course
        )

    def test_create_subscription(self):
        self.client.force_authenticate(user=self.test_user)

        # удачное создания подписки
        data = {"course": self.test_course.pk}
        response = self.client.post("/users/subscriptions/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["course"], self.test_course.pk)

        subscription = Subscription.objects.filter(
            user=self.test_user.pk, course=self.test_course.pk
        ).exists()
        self.assertEqual(subscription, True)

        # если подписка у пользователя уже есть, выдает ошибку с сообщением 'Эта подписка у вас уже есть'
        second_data = {"course": self.test_course.pk}
        response = self.client.post("/users/subscriptions/", data=second_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[0], "Эта подписка у вас уже есть")

    def test_check_subscribe_course(self):
        self.client.force_authenticate(user=self.test_user)

        response = self.client.get("/material/course/")
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["results"][1]["is_your_subscribe"], True)
        self.assertEqual(
            response.json()["results"][1]["subscribers"][0], self.test_user.email
        )
        self.assertEqual(response.json()["results"][0]["is_your_subscribe"], False)
        self.assertEqual(response.json()["results"][0]["subscribers"], [])

    def test_delete_subscribe_any_user(self):
        self.client.force_authenticate(user=self.test_second_user)

        response = self.client.delete(f"/users/subscriptions/{self.test_first_subscribe.pk}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json()["detail"], "У вас недостаточно прав для выполнения данного действия.")

    def test_delete_subscribe_for_user(self):
        self.client.force_authenticate(user=self.test_user)

        response = self.client.delete(f"/users/subscriptions/{self.test_first_subscribe.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        subscription = Subscription.objects.filter(user=self.test_user.pk, course=self.test_second_course.pk).exists()
        self.assertEqual(subscription, False)

    def tearDown(self):
        pass

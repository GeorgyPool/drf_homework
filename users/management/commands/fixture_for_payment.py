from django.core.management import BaseCommand
from django.db import IntegrityError

from material.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    """
    Команда для создания тестового пользователя и платежа
    """

    help = "Создает тестового пользователя"

    def handle(self, *args, **options):

        try:
            user = User.objects.create(
                email="user@example.com", username="example_user", phone_number="12345"
            )

            user.set_password("123")
            user.save()
            self.stdout.write(
                self.style.SUCCESS("Тестовый пользователь успешно создан")
            )

        except IntegrityError:
            self.stdout.write(self.style.WARNING("Пользователь уже создан"))

        try:
            Course.objects.create(
                title="Ведение бизнеса", description="Курс по ведению бизнеса"
            )
            Course.objects.create(
                title="Погружение в жизнь", description="Курс по погружению в жизнь"
            )

            Lesson.objects.create(
                title="Урок 1 по ведению бизнеса",
                description="Описание",
                course=Course.objects.get(title="Ведение бизнеса"),
            )

            Lesson.objects.create(
                title="Урок 2 по ведению бизнеса",
                description="Описание",
                course=Course.objects.get(title="Ведение бизнеса"),
            )

            Lesson.objects.create(
                title="Урок 1 по погружению в жизнь",
                description="Описание",
                course=Course.objects.get(title="Погружение в жизнь"),
            )
            self.stdout.write(self.style.SUCCESS("Курсы и уроки успешно созданы"))

        except IntegrityError as e:
            self.stdout.write(self.style.WARNING(f"Ошибка {e}"))

        try:
            Payment.objects.create(
                user=User.objects.get(email="user@example.com"),
                course=Course.objects.get(title="Ведение бизнеса"),
                price=20000.00,
                payment_method=Payment.transfer,
            )

            Payment.objects.create(
                user=User.objects.get(email="user@example.com"),
                lesson=Lesson.objects.get(title="Урок 1 по погружению в жизнь"),
                price=1000.00,
                payment_method=Payment.cash,
            )

            self.stdout.write(self.style.SUCCESS("Платеж успешно создан"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Уже создано"))

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from material.models import Course, Lesson


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    username = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Никнейм"
    )

    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    city = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Ваш город"
    )
    avatar = models.ImageField(upload_to="users/avatar/")

    USERNAME_FIELD = "email"


class Payment(models.Model):
    cash = "Наличные"
    transfer = "Перевод на счет"

    PAYMENT_CHOICES = [(cash, "Наличные"), (transfer, "Перевод на счет")]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_payment"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_payment",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_payment",
        blank=True,
        null=True,
    )

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")

    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма оплаты"
    )

    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_CHOICES, verbose_name="Метод оплаты"
    )

    def __str__(self):
        return f"{self.course if self.course else self.lesson}"

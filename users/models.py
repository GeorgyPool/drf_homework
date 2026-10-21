from django.contrib.auth.models import AbstractBaseUser
from django.db import models


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

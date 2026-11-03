from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import User


class Command(BaseCommand):
    help = """Команда для создания и проверки группы модераторов"""

    def handle(self, *args, **options):

        try:
            Group.objects.create(name="moderators")
            self.stdout.write(self.style.SUCCESS("Группа модераторов успешно создана"))
        except IntegrityError as e:
            self.stdout.write(self.style.WARNING(f"Такая группа уже существует: {e}"))

        try:
            user_moder = User.objects.create(email="user_moder@example.com")
            user_moder.set_password("user_moder123")
            user_moder.save()
            self.stdout.write(self.style.SUCCESS("Пользователь создан"))
        except IntegrityError as e:
            self.stdout.write(self.style.WARNING(f"Такой пользователь уже создан: {e}"))

        try:
            group_moder = Group.objects.get(name="moderators")
            user_moder = User.objects.get(email="user_moder@example.com")
            user_moder.groups.add(group_moder)
            self.stdout.write(
                self.style.SUCCESS("Пользователь с правами модератора успешно создан")
            )
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(
                    f"Во время создания пользователя произошла ошибка: {type(e)}"
                )
            )

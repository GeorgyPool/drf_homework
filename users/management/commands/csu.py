from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "создает супер пользователя"

    def handle(self, *args, **options):
        csu = User.objects.create_user(email="super@example.com", username="super")
        csu.save()
        csu.set_password("super123")
        csu.is_active = True
        csu.is_staff = True
        csu.is_superuser = True
        csu.save()
        self.stdout.write(self.style.SUCCESS("супер пользователь успешно создан"))

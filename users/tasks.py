from datetime import timedelta

from celery import shared_task
from django.utils import timezone


@shared_task()
def check_login_time():
    from .models import User

    time_off = timezone.now() - timedelta(days=30)
    User.objects.filter(last_login__lt=time_off).update(is_active=False)

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import Subscription


@shared_task()
def send_message_for_update_material_course(course_id, title):
    """Отправляет отложенную рассылку при обновлении материала курса."""

    recipient_list = list(
        Subscription.objects.filter(course=course_id).values_list(
            "user__email", flat=True
        )
    )
    if recipient_list:
        send_mail(
            subject="Новый материал по вашей подписке курса",
            message=f"новый урок: {title}",
            from_email=EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )

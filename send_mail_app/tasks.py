from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_mail_func():
    User = get_user_model()
    users = User.objects.all()
    #timezone.localtime(users.date_time)
    for user in users:

        mail_subject = 'Greetings from Celery'
        message = "This is a test mail sent using Celery task queue system in Django framework."
        to_mail = user.email

        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [to_mail],
            fail_silently = True,
        )

    return "Done"
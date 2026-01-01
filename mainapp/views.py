from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django.http import HttpResponse
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_view_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent")

def schedule_mail(request):
    # Schedule mail to be sent at 8 AM every day
    schedule, created = CrontabSchedule.objects.get_or_create(hour='8', minute='0')
    PeriodicTask.objects.create(crontab=schedule, name='Send Mail Every Day at 8 AM', task='send_mail_app.tasks.send_mail_func')
    return HttpResponse("Mail Scheduled at 8 AM Daily")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('sendmail/', views.send_mail_view_to_all, name='sendmail'),
    path('schedulemail/', views.schedule_mail, name='schedulemail'),
]

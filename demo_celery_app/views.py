from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
import os
from dotenv import load_dotenv
load_dotenv()
from django.core.mail import send_mail
# Create your views here.


def index(request):
    # sleepy(10)
    # sleepy.delay(10)
    # send_mail_without_celery()
    send_mail_task()
    return HttpResponse("<h1>Hello Django!</h1>")

def send_mail_without_celery():
    send_mail('Celery Worked',
              'Thank You CodeKeen',
              os.getenv('DEFAULT_FROM_EMAIL'),
              ['supritk16@gmail.com'], fail_silently=False)
    return None
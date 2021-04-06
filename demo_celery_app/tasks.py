from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import os
from dotenv import load_dotenv

load_dotenv()


@shared_task
def sleepy(duariton):
    sleep(duariton)
    return None


@shared_task
def send_mail_task():
    send_mail('Celery Worked',
              'Thank You CodeKeen',
              os.getenv('DEFAULT_FROM_EMAIL'),
              ['supritk16@gmail.com'], fail_silently=False)
    return None

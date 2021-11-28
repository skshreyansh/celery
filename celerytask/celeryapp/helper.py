from django.core.mail import  send_mail


# Create your views here.

def send_mail_without_celery():
    send_mail('celery worked', " Hii there from celery",
            "darkknighht1@gmail.com",
            ['skshreyansh1@gmail.com'],
            fail_silently=False
            )
    return None
from django.shortcuts import render

from django.http import HttpResponse
from .task import *
from .helper import *



def index(request):
    send_mail_task.delay()
    return HttpResponse("<h1>Hello , from celery</h1>") 


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = "Здравствуйте! Вы находитесь на сайте воспоминаний. \
        Если вы хотите сохранит или просмотреть свои впечатления о посещаяемых местах, " \
        "пожалуйста, авторизуйтесь через Facebook"
    return HttpResponse(text)

import logging

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Memory


def index(request):
    # Главная страница. Описание сайта и вход через facebook
    text = "Здравствуйте! Вы находитесь на сайте воспоминаний. \
        Если вы хотите сохранит или просмотреть свои впечатления о посещаяемых местах, " \
        "пожалуйста, авторизуйтесь через Facebook"
    return HttpResponse(text)


def personal_account(request):
    # Личный кабинет со списком воспоминаний или сообщением об их отсутствии
    latest_memories_list = Memory.objects.order_by('-pub_date')[:5]
    template = 'memories/user.html'
    context = {'latest_memories_list': latest_memories_list}
    return render(request, template, context)


def form_add_memory(request):
    # Форма добавления воспоминания
    template = 'memories/add_memory.html'
    title = "Добавление воспоминания"
    context = {'title': title}
    return render(request, template, context)


def save_memory(request):
    if request.method == 'POST':
        location = request.POST.get('searchTextField')
        print(location)
    template = 'memories/user.html'
    return render(request, template)

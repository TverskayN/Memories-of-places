import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Memory
from .forms import AddMemoryForm


def index(request):
    # Главная страница. Описание сайта и вход через facebook
    template = 'memories/index.html'
    title = "Добро пожаловать!"
    context = {'title': title}
    return render(request, template, context)


def personal_account(request):
    # Личный кабинет со списком воспоминаний или сообщением об их отсутствии
    latest_memories_list = Memory.objects.all()
    template = 'memories/user.html'
    title = "Ваши воспоминания"
    context = {
        'latest_memories_list': latest_memories_list,
        'title': title
    }
    return render(request, template, context)


def form_add_memory(request):
    # Форма добавления воспоминания
    template = 'memories/add_memory.html'
    title = "Добавление воспоминания"
    form = AddMemoryForm()
    context = {'title': title, 'form': form}
    return render(request, template, context)


def save_memory(request):
    # Проверка запонениия формы и сохранение воспоминания в БД
    if request.method == 'POST':
        form = AddMemoryForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['geo_point']:
                location_latitude, location_longitude, location_name, comment = get_new_nemory(form)
                save_new_memory_in_database(location_latitude, location_longitude, location_name, comment)
                return HttpResponseRedirect(reverse('memories:personal_account'))
    else:
        form = AddMemoryForm()
    return render(request, 'memories/add_memory.html', {
                'error_message': "Выберите место на карте",
                'form': form,
                })


def get_new_nemory(form):
    # Получает новое воспоминание (координаты, название и комментарий) из формы.
    # Возвращает координаты, название и комментарий нового воспоминания
    geo_point = form.cleaned_data['geo_point']
    location_latitude, location_longitude = geo_point.split(',')
    location_name = form.cleaned_data['location_name']
    comment = form.cleaned_data['comment']
    return location_latitude, location_longitude, location_name, comment


def save_new_memory_in_database(location_latitude,
                                location_longitude,
                                location_name,
                                comment):
    # Сохраняет координаты, название и комментарий нового воспоминания в БД
    # Пока приписывает новые воспоминания конкретному пользователю (user_id=1)
    memory = Memory(
        location_latitude=location_latitude,
        location_longitude=location_longitude,
        location_name=location_name,
        comment=comment,
        user_id=1,
    )
    memory.save()

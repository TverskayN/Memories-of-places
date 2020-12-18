from django.http import HttpResponse
from django.template import loader

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
    template = loader.get_template('memories/user.html')
    context = {'latest_memories_list': latest_memories_list}
    return HttpResponse(template.render(context))


def form_add_memory(request):
    # Форма добавления воспоминания
    return HttpResponse("Здесь вы можете добавить воспоминание")

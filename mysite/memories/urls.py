from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    url(r'^memories/$', views.personal_account, name='personal_account'),
    url(r'^add_memory/$', views.form_add_memory, name='form_add_memory')

]
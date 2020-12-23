from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'memories'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.personal_account, name='personal_account'),
    url(r'^save_memory/$', views.save_memory, name='save_memory'),
    url(r'^add_memory/$', views.form_add_memory, name='form_add_memory'),
]

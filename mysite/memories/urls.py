from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'memories'
urlpatterns = [
    # ex: /

    url('account/', views.personal_account, name='personal_account'),
    url('save_memory/', views.save_memory, name='save_memory'),
    url('add_memory/', views.form_add_memory, name='form_add_memory'),
    url('', views.index, name='index'),
]

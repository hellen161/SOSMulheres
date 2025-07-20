# app/urls_alerta_rapido.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.alerta_rapido_list, name='alerta_rapido_list'),
    path('novo/', views.alerta_rapido_create, name='alerta_rapido_create'),
]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
# Página inicial
    path('', views.home, name='home'),

    # Alerta Rápido
    path('alerta-rapido/', views.alerta_rapido_list, name='alerta_rapido_list'),
    path('alerta-rapido/novo/', views.alerta_rapido_create, name='alerta_rapido_create'),

    # Denúncia
    path('denuncia/', views.denuncia_list, name='denuncia_list'),
    path('denuncia/novo/', views.denuncia_create, name='denuncia_create'),

    # Rede de Apoio
    path('rede-apoio/', views.rede_apoio_list, name='rede_apoio_list'),
    path('rede-apoio/novo/', views.rede_apoio_create, name='rede_apoio_create'),

    # Informação
    path('informacao/', views.informacao_list, name='informacao_list'),
    path('informacao/novo/', views.informacao_create, name='informacao_create'),

    # Avaliação de Risco
    path('avaliacao-risco/', views.avaliacao_risco_list, name='avaliacao_risco_list'),
    path('avaliacao-risco/novo/', views.avaliacao_risco_create, name='avaliacao_risco_create'),
]

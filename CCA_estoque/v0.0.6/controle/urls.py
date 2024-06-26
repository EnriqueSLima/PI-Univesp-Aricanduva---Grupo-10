from django.urls import path, include
from . import views
import autenticar

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('inserir', views.inserir, name = 'inserir'),
    path('remover', views.remover, name = 'remover'),
    path('consultar', views.consultar, name = 'consultar'),
    path('estoque', views.estoque, name = 'estoque'),
    path('historico', views.historico, name = 'historico'),
    path('login', include('autenticar.urls')),
]
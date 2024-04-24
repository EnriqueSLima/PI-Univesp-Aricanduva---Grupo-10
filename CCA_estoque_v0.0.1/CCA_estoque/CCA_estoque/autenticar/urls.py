from django.urls import path, include
from . import views

urlpatterns = [
    path('autenticar', views.autenticar, name = 'autenticar'),
    path('cadastrar', views.cadastrar, name = 'cadastrar'),
    path('home', views.home, name = 'home'),

]
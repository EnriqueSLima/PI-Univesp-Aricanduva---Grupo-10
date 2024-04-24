from django.urls import path, include
from . import views
import autenticar

urlpatterns = [
    path('inserir', views.inserir, name = 'inserir'),
    #path('home', autenticar.views, name='home'),
    path('home', include('autenticar.urls')),
]
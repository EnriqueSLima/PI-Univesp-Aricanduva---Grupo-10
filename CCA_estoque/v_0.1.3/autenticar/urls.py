from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.autenticar, name='autenticar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
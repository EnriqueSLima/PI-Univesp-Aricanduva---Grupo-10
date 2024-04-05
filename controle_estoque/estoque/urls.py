from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inserir", views.inserir, name="inserir"),
    path("remover", views.remover, name="remover"),
]
from django.urls import path

from . import views
app_name = "estoque"
urlpatterns = [
    path("", views.index, name="index"),
    path("inserir", views.inserir, name="inserir"),
    path("remover", views.remover, name="remover"),
    path("detalhe", views.detalhe, name="detalhe"),

]
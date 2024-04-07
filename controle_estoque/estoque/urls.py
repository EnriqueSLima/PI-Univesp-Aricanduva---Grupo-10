from django.urls import path
from estoque.views import IndexView, InserirView, RemoverView,ConsultaView, DetalheView

from . import views

app_name = "estoque"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("inserir", InserirView.as_view(), name="inserir"),
    path("remover", RemoverView.as_view(), name="remover"),
    path("consultar", ConsultaView.as_view(), name="consultar"),
    path("detalhe", DetalheView.as_view, name="detalhe"),

]
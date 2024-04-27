from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import InserirForm
from .models import Uniforme, Core, Tipo, Tamanho

class IndexView(TemplateView):
    template_name = "estoque/index.html"

class InserirView(TemplateView):
    template_name =  "estoque/inserir.html"
    model = Uniforme
    fields = '__all__'
    context_object_name = 'uniformes'
    extra_context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
        'form' : InserirForm()
    }

class RemoverView(TemplateView):
    template_name =  "estoque/remover.html"
    extra_context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }

class ConsultaView(TemplateView):
    template_name =  "estoque/consulta.html"
    extra_context = {
        'uniformes' : Uniforme.objects.all(),
    }
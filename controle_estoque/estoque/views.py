from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Uniforme, Core, Tipo, Tamanho

def index(request):
    return render(request, "estoque/index.html")

def inserir(request):
    context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }
    return render(request, "estoque/inserir.html", context)

def remover(request):
    context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }
    return render(request, "estoque/remover.html", context)

def detalhe(request):
    context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }
    return render(request, "estoque/detalhe.html", context)
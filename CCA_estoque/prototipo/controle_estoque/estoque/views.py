from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .models import Uniforme, Core, Tipo, Tamanho


def index(request):
    return render(request, 'estoque/index.html')

def inserir(request):
    if request.method == 'GET':
        context = {
            'tipos' : Tipo.objects.all(),
            'tamanhos' : Tamanho.objects.all(),
            'cores' : Core.objects.all(),
            'qtd' : Uniforme.uquantidade,
        }
        return render(request, 'estoque/inserir.html', context)

def remover(request):
    if request.method == 'GET':
        context = {
            'tipos' : Tipo.objects.all(),
            'tamanhos' : Tamanho.objects.all(),
            'cores' : Core.objects.all(),
            'qtd' : Uniforme.uquantidade,
        }
        return render(request, 'estoque/remover.html', context)

def consulta(request):
    if request.method == 'GET':
        context = {
            'uniformes' : Uniforme.objects.all()
        }
        #uniformes = Uniforme.objects.all()
        return render(request, 'estoque/consulta.html', context)
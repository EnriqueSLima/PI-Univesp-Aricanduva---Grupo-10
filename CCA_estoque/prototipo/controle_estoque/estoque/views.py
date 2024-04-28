from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .models import Uniforme, Core, Tipo, Tamanho


def index(request):
    return render(request, 'estoque/index.html')

def inserir(request):
    context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }
    if request.method == 'GET':
        return render(request, 'estoque/inserir.html', context)
    # Caso o método for POST 
    else:
        #TODO: Implementar alteração no banco de dados
        tipo = request.POST.get('idutipo')
        tamanho = request.POST.get('idutamanho')
        cor = request.POST.get('iducor')
        qtd = request.POST.get('iduquantidade')

        return render(request, 'estoque/inserir.html', context)

def remover(request):
    context = {
        'tipos' : Tipo.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'cores' : Core.objects.all(),
        'qtd' : Uniforme.uquantidade,
    }
    if request.method == 'GET':
        return render(request, 'estoque/remover.html', context)

def consulta(request):
    context = {
        'uniformes' : Uniforme.objects.all()
    }
    if request.method == 'GET':
        return render(request, 'estoque/consulta.html', context)
    else:
        return render(request, 'estoque/consulta.html', context)
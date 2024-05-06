from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from django.db import models
from .models import Tipo, Estilo, Core, Tamanho, Uniforme

context = {
        'tipos' : Tipo.objects.all(),
        'estilos' : Estilo.objects.all(),
        'cores' : Core.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'qtd' : Uniforme.qtd,
        'uniforme' : Uniforme.objects.all()
    }

# AUTENTIFICAÇÃO REQUERIDA
@login_required(login_url = 'autenticar')
def home(request):
    return render(request, 'home.html')

@login_required(login_url = 'autenticar')
def inserir(request):
    if request.method == "GET":
        return render(request, 'inserir.html', context)
    else:
        tipo = request.POST.get('tipos')
        estilo = request.POST.get('estilos')
        cor = request.POST.get('cores')
        tamanho = request.POST.get('tamanhos')
        quantidade = request.POST.get('quantidade')
        
        #uniforme = Uniforme.objects.filter(tipo=tipo, estilo=estilo, cor=cor, tamanho=tamanho)
        #uniforme.qtd += quantidade
        #uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme inserido com sucesso.')

        return render(request, 'inserir.html', context)


@login_required(login_url = 'autenticar')
def remover(request):
    if request.method == "GET":
        return render(request, 'remover.html', context)
    else:
        tipo = request.POST.get('tipos')
        estilo = request.POST.get('estilos')
        cor = request.POST.get('cores')
        tamanho = request.POST.get('tamanhos')
        quantidade = request.POST.get('quantidade')
        
        #uniforme = Uniforme.objects.filter(tipo=tipo, estilo=estilo, cor=cor, tamanho=tamanho)
        #uniforme.qtd += quantidade
        #uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme removido com sucesso.')

        return render(request, 'remover.html', context)

@login_required(login_url = 'autenticar')
def consultar(request):
    if request.method == "GET":
        return render(request, 'consultar.html', context)
    else:
        return render(request, 'consultar.html', context)
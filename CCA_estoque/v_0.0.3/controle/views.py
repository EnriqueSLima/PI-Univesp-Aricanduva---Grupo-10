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
    }

# AUTENTIFICAÇÃO REQUERIDA
@login_required(login_url = 'autenticar')
def home(request):
    return render(request, 'home.html')

@login_required(login_url = 'autenticar')
def inserir(request):
    if request.method == "GET":
        return render(request, 'inserir.html', context)
    elif request.method == "POST":
        tipo = request.POST.get('tipos')
        estilo = request.POST.get('estilos')
        cor = request.POST.get('cores')
        tamanho = request.POST.get('tamanhos')
        qtd = int(request.POST.get('qtd'))

        uniforme = Uniforme (
            tipo = tipo,
            estilo = estilo,
            cor_id = cor,
            tamanho = tamanho,
            qtd = qtd
        )

        uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso.')

        return render(request, 'inserir.html', context)


@login_required(login_url = 'autenticar')
def remover(request):
    return render(request, 'remover.html', context)

@login_required(login_url = 'autenticar')
def consultar(request):
    return render(request, 'consultar.html', context)
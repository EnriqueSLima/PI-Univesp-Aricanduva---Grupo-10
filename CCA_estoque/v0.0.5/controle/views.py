from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from django.db import models
from .models import Tipo, Core, Tamanho, Uniforme

context = {
        'tipos' : Tipo.objects.all(),
        'cores' : Core.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'qtd' : Uniforme.qtd,
    }

# AUTENTIFICAÇÃO REQUERIDA
@login_required(login_url = 'autenticar')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='autenticar')
def inserir(request):
    if request.method == "GET":
        return render(request, 'inserir.html', context)
    else:
        tipo = request.POST.get('tipo')
        cor = request.POST.get('cor')
        tamanho = request.POST.get('tamanho')
        qtd = request.POST.get('qtd')

        uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho)
        uniforme.qtd += int(qtd)
        uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme inserido com sucesso.')
        return redirect('inserir')

@login_required(login_url = 'autenticar')
def remover(request):
    if request.method == "GET":
        return render(request, 'remover.html', context)
    else:
        tipo = request.POST.get('tipo')
        cor = request.POST.get('cor')
        tamanho = request.POST.get('tamanho')
        qtd = request.POST.get('qtd')
      
        uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho)
        uniforme.qtd -= int(qtd)
        uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme removido com sucesso.')

        return redirect('remover')

@login_required(login_url = 'autenticar')
def consultar(request):
    if request.method == "GET":
        return render(request, 'consultar.html', context)
    else:
        return render(request, 'consultar.html', context)
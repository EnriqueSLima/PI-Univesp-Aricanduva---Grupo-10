from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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
    return render(request, 'inserir.html', context)

@login_required(login_url = 'autenticar')
def remover(request):
    return render(request, 'remover.html', context)

@login_required(login_url = 'autenticar')
def consultar(request):
    return render(request, 'consultar.html', context)
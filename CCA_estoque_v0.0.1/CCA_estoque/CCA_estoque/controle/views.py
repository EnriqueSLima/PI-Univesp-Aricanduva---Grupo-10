from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# AUTENTIFICAÇÃO REQUERIDA
@login_required(login_url = 'autenticar')
def home(request):
    return render(request, 'home.html')

def inserir(request):
    return render(request, 'inserir.html')

def remover(request):
    return render(request, 'remover.html')

def consultar(request):
    return render(request, 'consultar.html')

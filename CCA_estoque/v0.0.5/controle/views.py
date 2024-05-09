from django.shortcuts import render, redirect
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

@login_required(login_url='autenticar')
def inserir(request):
    if request.method == "GET":
        return render(request, 'inserir.html', context)
    else:
        tipo = request.POST.get('tipo')  # Updated key
        estilo = request.POST.get('estilo')  # Updated key
        cor = request.POST.get('cor')  # Updated key
        tamanho = request.POST.get('tamanho')  # Updated key
        qtd = request.POST.get('qtd')
      
        uniforme = Uniforme.objects.get(tipo_id=tipo, estilo_id=estilo, cor_id=cor, tamanho_id=tamanho)  # Updated to use tipo_id, estilo_id, cor_id, tamanho_id
        uniforme.qtd += int(qtd)
        uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme inserido com sucesso.')

        return redirect('inserir')


#@login_required(login_url = 'autenticar')
#def inserir(request):
#    if request.method == "GET":
#        return render(request, 'inserir.html', context)
#    else:
#        tipo_id = request.POST.get('tipos')
#        estilo_id = request.POST.get('estilos')
#        cor_id = request.POST.get('cores')
#        tamanho_id = request.POST.get('tamanhos')
#        quantidade = request.POST.get('quantidade')
#        
#        try:
#            # Create a new Uniforme object with the provided data
#            uniforme = Uniforme.objects.create(
#                tipo_id=tipo_id,
#                estilo_id=estilo_id,
#                cor_id=cor_id,
#                tamanho_id=tamanho_id,
#                qtd=quantidade
#            )
#            messages.add_message(request, constants.SUCCESS, 'Uniforme inserido com sucesso.')
#        except Exception as e:
#            # Handle any exceptions that occur during object creation
#            messages.add_message(request, constants.ERROR, f'Erro ao inserir uniforme: {e}')
#
#        return redirect('inserir')  # Redirect back to the inserir page or any other URL


@login_required(login_url = 'autenticar')
def remover(request):
    if request.method == "GET":
        return render(request, 'remover.html', context)
    else:
        tipo = request.POST.get('tipo')  # Updated key
        estilo = request.POST.get('estilo')  # Updated key
        cor = request.POST.get('cor')  # Updated key
        tamanho = request.POST.get('tamanho')  # Updated key
        qtd = request.POST.get('qtd')
      
        uniforme = Uniforme.objects.get(tipo_id=tipo, estilo_id=estilo, cor_id=cor, tamanho_id=tamanho)  # Updated to use tipo_id, estilo_id, cor_id, tamanho_id
        uniforme.qtd -= int(qtd)
        uniforme.save()
        messages.add_message(request, constants.SUCCESS, 'Uniforme inserido com sucesso.')

        return redirect('remover')

@login_required(login_url = 'autenticar')
def consultar(request):
    if request.method == "GET":
        return render(request, 'consultar.html', context)
    else:
        return render(request, 'consultar.html', context)
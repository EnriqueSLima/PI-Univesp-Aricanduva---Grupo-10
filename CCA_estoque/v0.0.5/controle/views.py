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

        try:
            uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho)
            if uniforme:
                uniforme.qtd += int(qtd)
                uniforme.save()
                messages.success(request, 'Uniforme inserido com sucesso.')
        except Uniforme.DoesNotExist:
            uniforme = Uniforme.objects.create(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho, qtd=qtd)
            messages.success(request, 'Novo uniforme criado com sucesso.')
        except Exception as e:
            messages.error(request, f'Erro ao inserir: {e}')
        
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

        try:
            uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho)
            if uniforme:
                uniforme.qtd -= int(qtd)
                if uniforme.qtd < 0:
                    messages.warning(request, 'Quantidade maior que o estoque.')
                    return redirect('remover')
                uniforme.save()
                messages.success(request, 'Uniforme removido com sucesso.')
        except Uniforme.DoesNotExist:
            messages.error(request, 'Uniforme não cadastrado.')
        except Exception as e:
            messages.error(request, f'Erro ao remover: {e}')
        
        return redirect('remover')

@login_required(login_url = 'autenticar')
def consultar(request):
    context = {
        'uniformes': Uniforme.objects.all(),
        'tipos' : Tipo.objects.all(),
        'cores' : Core.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'qtd' : Uniforme.qtd,
    }

    tipo_filter = request.GET.get('tipo_filter')
    tamanho_filter = request.GET.get('tamanho_filter')
    cor_filter = request.GET.get('cor_filter')

    if request.method == "GET":
        return render(request, 'consultar.html', context)
    else:
        return redirect('consultar')

def test(request):
    context = {
        'uniformes': Uniforme.objects.all(),
        'tipos' : Tipo.objects.all(),
        'generos' : Genero.objects.all(),
        'cores' : Core.objects.all(),
        'tamanhos' : Tamanho.objects.all(),
        'qtd' : Uniforme.qtd,
    }

    tipo_filter = request.GET.get('tipo_filter')
    tamanho_filter = request.GET.get('tamanho_filter')
    cor_filter = request.GET.get('cor_filter')
    return render(request, 'test.html', context)
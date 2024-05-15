from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from django.db import models
from .models import Tipo, Genero, Core, Tamanho, Uniforme

context = {
    'uniformes': Uniforme.objects.all(),
    'generos' : Genero.objects.all(),
    'tipos' : Tipo.objects.all(),
    'cores' : Core.objects.all(),
    'tamanhos' : Tamanho.objects.all(),
    'qtd' : Uniforme.qtd,
    'local' : Uniforme.local,
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
        genero = request.POST.get('genero')
        qtd = request.POST.get('qtd')
        local = request.POST.get('local')

        try:
            uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho, genero_id=genero)
            if uniforme:
                uniforme.qtd += int(qtd)
                uniforme.save()
                messages.success(request, 'Uniforme inserido com sucesso.')
        except Uniforme.DoesNotExist:
            uniforme = Uniforme.objects.create(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho,genero_id=genero , qtd=qtd, local=local)
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
        genero = request.POST.get('genero')
        qtd = request.POST.get('qtd')
        local = request.POST.get('local')

        try:
            uniforme = Uniforme.objects.get(tipo_id=tipo, cor_id=cor, tamanho_id=tamanho, genero_id=genero)
            if uniforme:
                uniforme.qtd -= int(qtd)
                if uniforme.qtd < 0:
                    messages.success(request, 'Quantidade maior que o estoque.')
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
    uniformes = Uniforme.objects.all()
    generos = Genero.objects.all()
    tipos = Tipo.objects.all()
    cores = Core.objects.all()
    tamanhos = Tamanho.objects.all()

    tipo_filter = request.GET.get('tipo_filter')
    tamanho_filter = request.GET.get('tamanho_filter')
    cor_filter = request.GET.get('cor_filter')

    if tipo_filter and tipo_filter != '0':
        uniformes = uniformes.filter(tipo_id=tipo_filter)
    if tamanho_filter and tamanho_filter != '0':
        uniformes = uniformes.filter(tamanho_id=tamanho_filter)
    if cor_filter and cor_filter != '0':
        uniformes = uniformes.filter(cor_id=cor_filter)

    context = {
        'uniformes': uniformes,
        'generos': generos,
        'tipos': tipos,
        'cores': cores,
        'tamanhos': tamanhos,
    }
    return render(request, 'consultar.html', context)


def estoque(request):
    return render(request, 'estoque.html', context)

def historico(request):
        return render(request, 'historico.html', context)
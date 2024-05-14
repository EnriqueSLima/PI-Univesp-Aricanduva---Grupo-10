from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages

# CADASTRO DE USUÁRIOS SIMPLES
def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    else:
        cad_usuario = request.POST.get('usuario')
        cad_email = request.POST.get('email')
        cad_senha = request.POST.get('senha0')
        cad_senha1 = request.POST.get('senha1')
        # Verifica se já existe usuário com mesmo nome
        check_exist = User.objects.filter(username=cad_usuario).all()
        # Caso JÁ exista um usuário com este nome
        if check_exist:
            messages.add_message(request, constants.WARNING, 'Usuário já existe.')
            return redirect('cadastrar')
        # Caso a senha tenha menos de 6 caracteres
        if len(cad_senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 6 caracteres.')
            return redirect('cadastrar')
        # Caso as senhas sejam diferentes
        if cad_senha != cad_senha1:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais.')
            return redirect('cadastrar')
        # Caso NÃO haja conflitos com os IF's anteriores
        else:
            # Cria um novo usuário com os parametros do formulário e salva no banco de dados
            colaborador = User.objects.create_user(username=cad_usuario, email=cad_email, password=cad_senha)
            colaborador.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
            return redirect('cadastrar')

# AUTENTIFICAÇÃO DE USUÁRIOS
def autenticar(request):
    if request.method == 'GET':
        return render(request, 'autenticar.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha0')
        # Autentificação do usuário 
        auth_user = authenticate(request, username=usuario, password=senha)
        # Caso os parametros estejam corretos
        if auth_user:
            login(request, auth_user)
            return redirect('home')
        else:
            # Caso os parametros NÃO estejam corretos
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha incorretos.')
            return redirect('autenticar')
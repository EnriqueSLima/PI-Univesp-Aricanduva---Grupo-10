from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# CADASTRO DE USUÁRIOS SIMPLES
def cadastrar(request):
    if request.method == 'GET':
        # Caso o método for GET retona a pagina de cadastro
        return render(request, 'cadastrar.html')
    else:
        # Caso o método for POST 
        cad_usuario = request.POST.get('usuario')
        cad_email = request.POST.get('email')
        cad_senha = request.POST.get('senha0')
        # Verifica se já existe usuário com mesmo nome
        check_exist = User.objects.filter(username=cad_usuario).all()
        # Caso JÁ exista um usuário com este nome
        if check_exist:
            return render(request, 'cadastrar.html')
        # Caso NÃO exista um usuário com este nome
        else:
            # Cria um novo usuário com os parametros do formulário e salva no banco de dados
            colaborador = User.objects.create_user(username=cad_usuario, email=cad_email, password=cad_senha)
            colaborador.save()
        return render(request, 'autenticar.html')

# AUTENTIFICAÇÃO DE USUÁRIOS
def autenticar(request):
    if request.method == 'GET':
        # Caso o método for GET retona a pagina de login
        return render(request, 'autenticar.html')
    else:
        # Caso o método for POST 
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha0')
        # Autentificação do usuário 
        auth_user = authenticate(username=usuario, password=senha)
        # Caso os parametros estejam corretos
        if auth_user:
            login(request, auth_user)
            return render(request, 'home.html')
        else:
            # Caso os parametros NÃO estejam corretos
            return render(request, 'autenticar.html')



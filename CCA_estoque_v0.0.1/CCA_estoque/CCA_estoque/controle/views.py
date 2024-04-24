from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'autenticar')
def inserir(request):
    return render(request, 'inserir.html')

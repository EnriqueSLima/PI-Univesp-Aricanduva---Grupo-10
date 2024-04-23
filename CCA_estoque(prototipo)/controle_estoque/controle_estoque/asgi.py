""" 
mysite/asgi.py: um ponto de integração para servidores web compatíveis com ASGI usado para servir seu projeto.
Veja Como fazer o deploy com ASGI para mais detalhes em https://docs.djangoproject.com/pt-br/5.0/howto/deployment/asgi/.
 """

"""
ASGI config for controle_estoque project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_estoque.settings')

application = get_asgi_application()

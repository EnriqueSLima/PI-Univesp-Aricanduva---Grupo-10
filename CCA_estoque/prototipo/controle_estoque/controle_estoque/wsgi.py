""" 
mysite/wsgi.py: um ponto de integração para servidores web compatíveis com WSGI usado para servir seu projeto. 
Veja Como implementar com WSGI para mais detalhes em https://docs.djangoproject.com/pt-br/5.0/howto/deployment/wsgi/.
 """

"""
WSGI config for controle_estoque project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_estoque.settings')

application = get_wsgi_application()

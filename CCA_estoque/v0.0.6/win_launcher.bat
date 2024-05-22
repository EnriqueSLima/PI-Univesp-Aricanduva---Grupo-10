@echo off
cd /caminho/do/seu/diretorio
start cmd /k python manage.py runserver
ping 127.0.0.1 -n 5 > nul
start http://localhost:8000/login/auth
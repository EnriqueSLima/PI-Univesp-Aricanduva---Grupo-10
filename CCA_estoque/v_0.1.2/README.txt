**Para criar um ambiente virtual**

- SO Linux:
    python3 -m venv venv

- SO Windows:
    python -m venv venv


**Para ativar um ambiente virtual**

- SO Linux:
    source venv/bin/activate

- SO Windows:
    venv\Scripts\Activate

    OBS: Caso algum comando retorne um erro de permissão execute o código e tente novamente:

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


** Dependências do projeto **

- python 3.11
- Django 5.0
- mssql-django


** Para rodar o servidor **

No diretório v_0.1.2 onde está o arquivo manage.py, execute o comando:

- SO Linux:
    python3 manage.py runserver

- SO Windows:
    python manage.py runserver

Deposi acesse o servidor local na porta 8000.
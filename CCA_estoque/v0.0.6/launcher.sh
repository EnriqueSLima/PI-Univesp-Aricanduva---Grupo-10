#!/bin/bash
cd /home/snowfox/GitHub/PI-Univesp-Aricanduva---Grupo-10/CCA_estoque/v0.0.6
python3 manage.py runserver &
sleep 3  # Espera 5 segundos para garantir que o servidor esteja pronto
xdg-open http://localhost:8000/login/auth

#!/bin/bash

# Iniciar o Gunicorn em segundo plano
gunicorn --workers 3 --bind 0.0.0.0:8080 app:app &

# Iniciar o Apache2 em primeiro plano
apache2ctl -D FOREGROUND

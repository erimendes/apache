# # Usar uma imagem base do Python com o Apache
# FROM python:3.9-slim

# # Instalar dependências do sistema operacional e Apache
# RUN apt-get update \
#     && apt-get install -y apache2 \
# # && apt-get install -y libapache2-mod-proxy-html \
#     && apt-get install -y libxml2-dev \
#     && apt-get install -y gcc \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Instalar o Gunicorn, Flask e outras dependências do Python
# RUN pip install --no-cache-dir gunicorn flask

# # Definir o diretório de trabalho no contêiner
# WORKDIR /app

# # Copiar os arquivos de código da aplicação
# COPY . /app/

# # Expor a porta 80 (para Apache)
# EXPOSE 80

# # Ativar os módulos do Apache
# RUN a2enmod proxy && \
#     a2enmod proxy_http && \
#     a2enmod rewrite && \
#     a2enmod proxy_html

# # Copiar o arquivo de configuração do Apache
# COPY apache-config.conf /etc/apache2/sites-available/000-default.conf

# # Iniciar o Gunicorn na porta 8000 (ou usar um socket Unix)
# CMD gunicorn --workers 3 --bind unix:/tmp/gunicorn.sock wsgi:app & apache2ctl -D FOREGROUND


# Usar uma imagem base do Python com o Apache
FROM python:3.9-slim

# Instalar dependências necessárias
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Ativar os módulos necessários do Apache
RUN a2enmod proxy && \
    a2enmod proxy_http && \
    a2enmod proxy_balancer && \
    a2enmod lbmethod_byrequests

# Reiniciar o Apache (no caso de precisar)
RUN service apache2 restart

# Instalar o Gunicorn, Flask e outras dependências do Python
RUN pip install --no-cache-dir gunicorn flask

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos de código da aplicação
COPY . /app/

# Expor a porta 80 para Apache
EXPOSE 80

# Ativar os módulos do Apache
# Ativar os módulos do Apache
RUN a2enmod proxy && \
    a2enmod proxy_http && \
    a2enmod proxy_balancer && \
    a2enmod lbmethod_byrequests && \
    a2enmod rewrite

# Copiar a configuração personalizada do Apache
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf

# Iniciar o Gunicorn na porta 8000 (ou qualquer outra porta ou socket desejado)
CMD gunicorn --workers 3 --bind 0.0.0.0:8000 app.wsgi:app & apache2ctl -D FOREGROUND
# CMD gunicorn --workers 3 --bind unix:/tmp/gunicorn.sock app.wsgi:app

# Usar a imagem oficial do Python
FROM python:3.9-slim

# Instalar dependências do sistema, incluindo Apache e módulos necessários
RUN apt-get update && \
    apt-get install -y apache2 \
    # libapache2-mod-proxy-html \
    libapache2-mod-fcgid \
    libxml2-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar as dependências do Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar o código da aplicação e o arquivo de configuração do Apache para o container
COPY . /usr/app/prov/script

# Definir o diretório de trabalho
WORKDIR /usr/app/prov/script

# Ativar módulos do Apache
RUN a2enmod proxy && \
    a2enmod proxy_http && \
    a2enmod rewrite && \
    a2enmod proxy_fcgi && \
    a2enmod headers

# Copiar a configuração do Apache para o container
COPY ./sites-available/apache2.conf /etc/apache2/sites-available/000-default.conf

# Expor a porta 80 para o Apache
EXPOSE 81

# Comando para iniciar o Apache e o Gunicorn simultaneamente
CMD gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app & apache2ctl -D FOREGROUND

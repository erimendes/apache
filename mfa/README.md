Passos para Iniciar um Novo Projeto Django com MariaDB e Django-Allauth:

1. Criação do Ambiente Virtual:
   Criação de um ambiente virtual é uma prática recomendada para isolar as dependências do seu projeto.
   
   Comandos:
   python3 -m venv venv  # Cria o ambiente virtual
   source venv/bin/activate  # Ativa o ambiente virtual

2. Instalação de Dependências:
   Instale o Django e outros pacotes necessários, como django-allauth, django-otp e pyotp.
   
   Comandos:
   pip install django
   pip install django-allauth
   pip install django-otp pyotp

3. Criação do Projeto Django:
   Para criar um novo projeto Django:

   Comandos:
   django-admin startproject mfa  # ou python3 -m django startproject mfa
   cd mfa/

4. Configuração do Banco de Dados:
   Você está usando o MariaDB, então certifique-se de que ele esteja instalado e funcionando.

   Comandos:
   sudo systemctl start mariadb  # Inicia o MariaDB
   mariadb -u root -p  # Conecte-se ao MariaDB

   Criar o banco de dados no MariaDB:
   CREATE DATABASE mfa;
   CREATE USER 'mfauser'@'localhost' IDENTIFIED BY 'sua_senha';
   GRANT ALL PRIVILEGES ON mfa.* TO 'mfauser'@'localhost';
   FLUSH PRIVILEGES;

5. Configuração do Django para o MariaDB:
   No arquivo settings.py do Django, altere a configuração do banco de dados para MariaDB.

   Exemplo no settings.py:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'mfa',
           'USER': 'mfauser',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

   Instale o driver MySQL para Python:
   pip install mysqlclient
   Ou, se preferir usar PyMySQL:
   pip install pymysql

   E adicione no seu __init__.py:
   import pymysql
   pymysql.install_as_MySQLdb()

6. Migrações e Criação de Aplicativos:
   Execute as migrações do Django:

   Comandos:
   python manage.py migrate  # Aplica as migrações iniciais

   Crie um novo aplicativo (como o accounts para autenticação):
   python manage.py startapp accounts

   Registre o aplicativo accounts no seu INSTALLED_APPS no settings.py:
   INSTALLED_APPS = [
       ...
       'accounts',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'django_otp',
       'allauth',
       'allauth.account',
       'allauth.socialaccount',
   ]

7. Migrações e Rodar o Servidor:
   Execute as migrações novamente, pois você pode ter que aplicar as migrações para o seu novo aplicativo (accounts):

   Comandos:
   python manage.py makemigrations
   python manage.py migrate

   Agora, execute o servidor Django para verificar se está funcionando:
   python manage.py runserver

8. Verificação de Dependências e Testes:
   Certifique-se de que as dependências estão corretamente instaladas e que o servidor do Django está funcionando. Você pode também verificar as URLs do seu aplicativo e testá-las.

Problemas Comuns e Soluções:
- Problemas com mysqlclient: Certifique-se de que os pacotes necessários para compilar o mysqlclient estão instalados no seu sistema:
  
  Comandos:
  sudo apt-get install pkg-config libmysqlclient-dev

- Problemas com o banco de dados: Certifique-se de que as credenciais e a configuração do banco de dados no settings.py estejam corretas e que o MariaDB ou MySQL esteja em execução.

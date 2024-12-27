"""
URL configuration for mfa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# mfa/mfa/urls.py
from django.contrib import admin
from django.urls import path, include
# Altere para o import correto, provavelmente de 'accounts.views'
from accounts import views  # Aqui, estamos importando o módulo 'views' do app 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Inclui as URLs de allauth
    path('', views.home, name='home'),  # Ou qualquer outra URL que você tenha para a home
    path('accounts/', include('accounts.urls')),  # Incluindo as URLs do app 'accounts'
]

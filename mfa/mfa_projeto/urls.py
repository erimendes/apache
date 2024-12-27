# mfa/mfa/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # URL para o app de autenticação
    path('accounts/', include('allauth.urls')),  # URLs do allauth (login, signup, etc.)
]


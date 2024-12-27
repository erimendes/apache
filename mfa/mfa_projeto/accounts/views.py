from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile
import random
import pyotp

from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Limpa a sessão do usuário
    return redirect('home')  # Redireciona para a página inicial ou para a página de login

def login_view(request):
    # Se o usuário já estiver logado, redireciona para a página inicial
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Se o usuário tiver TOTP configurado, vamos verificar o código TOTP
            if user.profile.totp_secret:
                return redirect('verify_totp')
            else:
                # Envia um e-mail de verificação e armazena o código no perfil do usuário
                code = send_verification_email(user.email)
                user.profile.verification_code = code  # Armazena o código de verificação
                user.profile.save()
                return redirect('verify_email')
        else:
            messages.error(request, "Credenciais inválidas.")
    
    return render(request, 'accounts/login.html')  # Corrigido para login.html

def verify_email(request):
    if request.method == 'POST':
        code = request.POST['code']
        if validate_email_code(request.user, code):
            # O código de e-mail foi validado, redireciona para a página inicial
            return redirect('home')
        else:
            messages.error(request, "Código inválido.")
    
    return render(request, 'accounts/verify_email.html')

def verify_totp(request):
    if request.method == 'POST':
        code = request.POST['code']
        if request.user.profile.verify_totp(code):
            # O código TOTP foi validado, redireciona para a página inicial
            return redirect('home')
        else:
            messages.error(request, "Código TOTP inválido.")
    
    return render(request, 'accounts/verify_totp.html')

def validate_email_code(user, code):
    # Validação de código por e-mail
    if user.profile.verification_code == int(code):
        return True
    return False

def send_verification_email(user_email):
    # Função para enviar o código de verificação por e-mail
    code = random.randint(100000, 999999)  # Gera um código aleatório
    subject = "Código de Verificação"
    message = f"Seu código de verificação é: {code}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])
    return code

def home(request):
    return render(request, 'home.html')  # Página inicial após o login

# Métodos auxiliares para TOTP
def generate_totp_secret(user):
    # Gera um segredo TOTP para o usuário
    totp = pyotp.TOTP(pyotp.random_base32())
    user.profile.totp_secret = totp.secret
    user.profile.save()

def verify_totp_secret(user, code):
    # Verifica o código TOTP fornecido
    totp = pyotp.TOTP(user.profile.totp_secret)
    return totp.verify(code)

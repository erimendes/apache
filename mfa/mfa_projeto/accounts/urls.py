# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Corrigido: importando auth_views corretamente

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('login/', views.login_view, name='account_login'),  # URL do login
    path('logout/', views.logout_view, name='logout'),  # URL do logout
    path('accounts/verify_email/', views.verify_email, name='verify_email'),  # URL de verificação de e-mail
    path('accounts/verify_totp/', views.verify_totp, name='verify_totp'),  # URL de verificação TOTP

    # URLs para redefinir a senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

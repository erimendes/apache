from django.db import models
from django.contrib.auth.models import User
import pyotp

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totp_secret = models.CharField(max_length=16, blank=True, null=True)

    def generate_totp_secret(self):
        totp = pyotp.TOTP(pyotp.random_base32())  # Gera um segredo aleatório
        self.totp_secret = totp.secret
        self.save()
        return totp.provisioning_uri(self.user.username, issuer_name="MySite")

    def verify_totp(self, code):
        totp = pyotp.TOTP(self.totp_secret)
        return totp.verify(code)

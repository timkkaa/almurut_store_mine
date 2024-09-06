from django.contrib.auth.models import BaseUserManager

class CustomUserManage(BaseUserManager):
    def crsate_user(self, email, password, **extra_fils):
        user = self.model(email=email, **extra_fils)
        user.set_password()
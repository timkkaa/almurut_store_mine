from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        unique=True,
        db_index=True,
    )
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=25)

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    password = models.TextField()

    phone_number = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )

    address = models.TextField()
    avatar = models.ImageField()

    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()

    birthadate = models.DateField()

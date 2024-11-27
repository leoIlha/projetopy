from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Usuarios(AbstractBaseUser):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False) #SUPERUSER
    is_active = models.BooleanField(default=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)

    REQUIRED_FIELDS = [ 'email']
    USERNAME_FIELD = 'nome'


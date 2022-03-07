from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_username(self):
        return self.email
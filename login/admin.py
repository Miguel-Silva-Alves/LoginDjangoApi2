from django.contrib import admin
from login.models import Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)

# Register your models here.

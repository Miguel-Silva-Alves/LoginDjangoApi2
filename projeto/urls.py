"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from rest_framework import routers
from login.views import ListaUsuarios, UsuariosViewSet
from requisicoes import views

router = routers.DefaultRouter()
router.register('register_user', UsuariosViewSet, basename='Register Login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('', include(router.urls)),
    path('register_user/', ListaUsuarios.as_view()),
    path('requisicoes/',views.RequisicoesView().as_view(), name='requisicoes'),
]
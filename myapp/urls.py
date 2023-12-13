# myapp/urls.py
from django.urls import path
from .views import user_login, registrar_usuario, bienvenida

urlpatterns = [
    path('', user_login, name='user_login'),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    path('bienvenida/', bienvenida, name= 'bienvenida'),
]
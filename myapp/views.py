# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistroForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la página principal o a la que desees después del inicio de sesión
                return redirect('bienvenida')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bienvenida')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def bienvenida(request):
    return render(request, 'bienvenida.html')
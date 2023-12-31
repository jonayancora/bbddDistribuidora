# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistroForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
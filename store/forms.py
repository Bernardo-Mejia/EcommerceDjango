from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control my-2 w-100', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control my-2 w-100', 'placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control my-2 w-100', 'placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control my-2 w-100', 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
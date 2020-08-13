from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NameForm(forms.Form):
    name = forms.CharField(max_length=20)


# ,widget=forms.Textarea(attrs={'cols': 25, 'rows': 2,'size': '40'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
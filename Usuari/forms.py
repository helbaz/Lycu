from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registrarUsuari(UserCreationForm):
    correu = forms.EmailField()
    imatge = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class novaSessio(User):
    username = forms.CharField(max_length=50, required=True)
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())


from django import forms
from .models import *


class formulariCuriositat(forms.Form):
    titol = forms.CharField(required=True)
    contingut = forms.CharField(widget=forms.Textarea, required=True)
    imatge = forms.ImageField(required=True)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())


class formulariCategoria(forms.Form):
    categoria =forms.CharField(required=True)


class crearComentari(forms.Form):
    textcuriositat = forms.CharField(required=True)
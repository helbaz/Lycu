# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse

from Usuari.models import Usuaris
from .forms import *


# Create your views here.
def registre(request):
    form = registrarUsuari(request.POST, request.FILES)
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('Index'))
    context = {'formulari': form}
    if request.method == 'POST':
        context = {'formulari': form, 'es_post': True}
        print(form.errors)
        print("\n\n")
        print(form.non_field_errors())
        if form.is_valid():
            #form.save(commit=False)
            nom_usuari = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            correu = form.cleaned_data.get('correu')
            imatge = form.cleaned_data.get('imatge')
            print(nom_usuari + " " + password)
            user1 = User(username=nom_usuari)
            user1.set_password(password)
            user1.save()
            if form.cleaned_data.get('imatge') is None:
                print("No tiene imagen")
                Usuaris.objects.create(usuari=user1, correu=correu)
            else:
                print("Tiene imagen")
                Usuaris.objects.create(usuari=user1, correu=correu, imatge_perfil=imatge)
            usuari = authenticate(username=nom_usuari, password=password)

            login(request, usuari)
            return HttpResponseRedirect(reverse('Index'))

    return render(request, 'Registra.html', context)



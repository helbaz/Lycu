# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User

from Usuari.models import *
from LycuMain.models import *
from django.shortcuts import render
from .forms import *

from .models import *


# Create your views here.
def index(request):
    form = crearComentari(request.POST)
    curiositats = Curiositat.objects.filter(estat=2).order_by('-data')[0]
    comentaris = Comentari.objects.all().filter(curiositat_comentada=curiositats).order_by('-data_comentari')
    context = {'curiositat': curiositats,
               'css': '../media/Index-style.css', 'form': form, 'comentaris': comentaris}
    if request.user.is_authenticated():
        usuari = Usuaris.objects.get(usuari=request.user)
        context = {'curiositat': curiositats, 'nom_usuari': request.user.username, 'css': '../media/Index-style.css',
                   'usuari': usuari, 'form': form, 'comentaris': comentaris}
    return render(request, 'Index.html', context)


# @login_required
# def publicar(request):

@login_required()
def publicarCuriositat(request):
    form = formulariCuriositat(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # form.save(commit=False)
            usuari = User.objects.get(username=request.user.username)
            usuari2 = Usuaris.objects.get(usuari=usuari)
            titol = form.cleaned_data.get('titol')
            contingut = form.cleaned_data.get('contingut')
            imatge = form.cleaned_data.get('imatge')
            curiositat = Curiositat(titol=titol, imatge=imatge, contingut=contingut, estat=2, autor=usuari2)
            curiositat.save()
            return HttpResponseRedirect(reverse('Index'))
    formCategoria = formulariCategoria(request.POST)
    context = {'formulari': form, 'formulario_categoria': formCategoria}
    if request.user.is_authenticated:
        context['usuari'] = Usuaris.objects.get(usuari=request.user)
        context['nom_usuari'] = request.user.username
    if formCategoria.is_valid():
        nom_categoria = formCategoria.cleaned_data.get('categoria')
        Categoria.objects.create(nom=nom_categoria)
        context['categoria_creada'] = True
        context['formulario_categoria'] = formCategoria
        return HttpResponseRedirect(reverse('publicar'))
    return render(request, 'Proposar.html', context)


def curiositat(request, curiositat_id):
    form = crearComentari(request.POST)
    curiositat = Curiositat.objects.get(pk=curiositat_id)
    comentaris = Comentari.objects.all().filter(curiositat_comentada=curiositat).order_by('-data_comentari')
    if request.user.is_authenticated():
        usuari = User.objects.get(username=request.user.username)
        usuari2 = Usuaris.objects.get(usuari=usuari)
        context = {'curiositat': curiositat, 'nom_usuari': request.user.username, 'css': '../media/Index-style.css',
                   'usuari': usuari2, 'form': form, 'comentaris': comentaris}
        if request.method == 'POST':
            if form.is_valid():
                comentari =  form.cleaned_data.get('textcuriositat')
                Comentari.objects.create(contingut=comentari, usuari_comenta=usuari2, curiositat_comentada=curiositat)
                return render(request, 'Index.html', context)
    else:
        context = {'curiositat': curiositat, 'comentaris': comentaris}
    return render(request, 'curiositat.html', context)


def biblioteca(request):
    ultimes_curiositats = Curiositat.objects.order_by('-data')
    #    template = loader.get_template('../templates/NomesCuriositat.html')
    biblio = {
        'ultimes_curiositats': ultimes_curiositats,
    }
    if request.user.is_authenticated():
        usuari = User.objects.get(username=request.user.username)
        biblio['nom_usuari'] = request.user.username
        biblio['usuari'] = Usuaris.objects.get(usuari=usuari)
    return render(request, 'Biblioteca.html', biblio)

import json
def buscador(request):
    if request.method == "GET":
        text = request.GET.get('busca')
        curiositats = Curiositat.objects.filter(titol__contains=text)
        llista = [ serializer(curiositatIndividual) for curiositatIndividual in curiositats ]
        return HttpResponse(json.dumps(llista), content_type='aplication/json')
    HttpResponseRedirect(reverse('Index'))


def serializer(curiositats):
    print curiositats
    return {'id': curiositats.id, 'titol': curiositats.titol, 'imatge': curiositats.imatge.url}
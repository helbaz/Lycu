# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.
class Categoria(models.Model):
    nom = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return self.nom


class Curiositat(models.Model):
    titol = models.CharField(max_length=40, blank=False, unique=True)
    imatge = models.ImageField(upload_to='Imatges/', blank=False)
    contingut = models.CharField(max_length=5000, blank=False)
    data = models.DateTimeField(default=timezone.now)
    estat = models.IntegerField(default=0)
    autor = models.ForeignKey('Usuari.Usuaris', on_delete=models.CASCADE)
    categoria_a_cusiositat = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    usuari_a_vot = models.ManyToManyField('Curiositat', through='Vot')

    def __str__(self):
        return self.titol

class Vot(models.Model):
    ha_votat = models.BooleanField(default=False)
    tipus = models.BooleanField (default=False)
    usuari_vota = models.ForeignKey('Usuari.Usuaris', on_delete=models.CASCADE)
    curiositat_votada = models.ForeignKey('Curiositat', on_delete=models.CASCADE)


class Comentari(models.Model):
    contingut = models.CharField(max_length=500)
    data_comentari = models.DateTimeField(default=timezone.now)
    usuari_comenta = models.ForeignKey('Usuari.Usuaris', on_delete=models.CASCADE, default=1)
    curiositat_comentada = models.ForeignKey('Curiositat', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.contingut

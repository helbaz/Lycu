# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuaris(models.Model):
    usuari = models.OneToOneField(User, on_delete=models.CASCADE)
    correu = models.CharField(max_length=50, blank=False, unique=True)
    imatge_perfil = models.ImageField(upload_to='Perfil_Usuari/', default='../../media/Perfil_Usuari'
                                                                          '/Usuari_default.png', blank=True)
    comentari_a_usuari = models.ManyToManyField('Usuaris', through='LycuMain.Comentari')

    def __str__(self):
        return self.usuari.username

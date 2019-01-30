from django.db import models


# Create your models here.
class Usuaris(models.Model):
    nom_usuari = models.CharField(max_length=20, blank=False)
    contrasenya = models.CharField(max_length=20, blank=False)
    correu = models.CharField(max_length=50, blank=False)
    permissos = models.BooleanField(default=False)
    usuari_a_vots = models.ManyToManyField('LycuMain.Curiositat', through='LycuMain.Vots')

    def __str__(self):
        return self.nom_usuari + " " + self.correu

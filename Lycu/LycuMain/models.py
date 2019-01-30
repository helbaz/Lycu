from django.db import models
from django.utils import timezone


# Create your models here.
class Categoria(models.Model):
    nom = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nom

class Curiositat(models.Model):
    titol = models.CharField(max_length=40, blank=False)
    imatge = models.ImageField(upload_to='Imatges/', blank=False)
    contingut = models.CharField(max_length=5000, blank=False)
    data = models.DateTimeField(default=timezone.now)
    estat = models.IntegerField(default=0)
    comentari_a_usuari = models.ManyToManyField('Usuari.Usuaris', through='Comentari')
    categoria_a_cusiositat = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titol


class Vots(models.Model):
    usuari_vota = models.ForeignKey('Usuari.Usuaris', on_delete=models.CASCADE)
    curiositat_votada = models.ForeignKey('Curiositat', on_delete=models.CASCADE)
    ha_votat = models.BooleanField(default=False)
    tipus = models.BooleanField(default=True)

    def __str__(self):
        return self.ha_votat

class Comentari(models.Model):
    contingut = models.CharField(max_length=500)
    data_comentari = models.DateTimeField(default=timezone.now)
    usuari_comenta = models.ForeignKey('Usuari.Usuaris', on_delete=models.CASCADE, default=1)
    curiositat_comentada = models.ForeignKey('Curiositat', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.contingut
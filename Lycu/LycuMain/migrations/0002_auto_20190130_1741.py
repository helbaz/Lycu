# Generated by Django 2.1.3 on 2019-01-30 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuari', '0001_initial'),
        ('LycuMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentari',
            name='curiositat_comentada',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='LycuMain.Curiositat'),
        ),
        migrations.AddField(
            model_name='comentari',
            name='usuari_comenta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Usuari.Usuaris'),
        ),
        migrations.AddField(
            model_name='curiositat',
            name='comentari_a_usuari',
            field=models.ManyToManyField(through='LycuMain.Comentari', to='Usuari.Usuaris'),
        ),
    ]

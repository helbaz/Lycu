# Generated by Django 2.1.3 on 2019-01-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LycuMain', '0007_vots'),
        ('Usuari', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuaris',
            name='usuari_a_vots',
            field=models.ManyToManyField(through='LycuMain.Vots', to='LycuMain.Curiositat'),
        ),
    ]

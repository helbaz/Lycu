# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Comentari)
admin.site.register(Curiositat)
admin.site.register(Vots)

"""Lycu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib.auth import views as auth_views

from LycuMain.views import *
from Usuari.views import *
app_name = 'url'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='Index'),
    url(r'^registre', registre, name='registre'),
    url(r'^login/$', auth_views.login, {'template_name': 'iniciarsessio.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'Index'}, name='sortir'),
    url(r'publicar', publicarCuriositat, name="publicar"),
    url(r'^biblioteca/$', biblioteca, name='biblioteca'),
    url(r'curiositat/(?P<curiositat_id>[0-9]+)', curiositat, name='curiositat'),
    url(r'buscador', buscador, name='buscador')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

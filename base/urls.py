from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from base.views import base
from blocks.views import slider

urlpatterns = [
    url(r'^base$', base),
    url(r'^slider$', slider),
]

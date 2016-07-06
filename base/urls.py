from django.conf.urls import url
from django.conf import settings

from base.views import base
from blocks.views import slider
from menu.views import menu

urlpatterns = [
    url(r'^base$', base),
    url(r'^slider$', slider),
    url(r'^menu(?P<path>[\d]*)$', menu)
]

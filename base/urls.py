from django.conf.urls import url

from base.views import base, app
from blocks.views import slider
from menu.views import menu
from staff.views import like

urlpatterns = [
    url(r'^base$', base),
    url(r'^slider$', slider),
    url(r'^menu$', menu),
    url(r'^app/(?P<slug>[\w]+)$', app),
    url(r'^app/(?P<slug>[\w]+)/(?P<id>[\w]+)$', app),
    url(r'^like$', like)
]

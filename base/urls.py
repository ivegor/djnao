from django.conf.urls import url
from django.conf import settings

from base.views import base, app
from blocks.views import slider
from detail.views import detail
from menu.views import menu
from staff.views import staff

urlpatterns = [
    url(r'^base$', base),
    url(r'^slider$', slider),
    url(r'^menu$', menu),
    url(r'^app/(?P<path>[\S]+)$', app),
    url(r'^detail/(?P<slug>[\S]+)$', detail),
    url(r'^staff$', staff)
]

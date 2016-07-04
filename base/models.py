from django.db import models

from djanao.models import BaseModel


class Base(BaseModel):
    heading = models.CharField(max_length=128)
    small_heading = models.CharField(max_length=32, blank=True)
    logo = models.ImageField()
    fav_icon = models.ImageField()
    phone = models.PositiveSmallIntegerField()

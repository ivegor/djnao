from django.db import models

from djanao.models import BaseModel


class Slider(BaseModel):
    h3 = models.CharField(max_length=255, blank=True)
    p = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='slider')

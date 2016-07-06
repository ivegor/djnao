from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from djanao.models import BaseModel


class Slider(BaseModel):
    h3 = models.CharField(max_length=255, blank=True)
    p = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    image = ProcessedImageField(upload_to='slider', processors=[ResizeToFill(1000, 400)])

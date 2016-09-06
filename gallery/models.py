from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from djanao.models import BaseModel


class PhotoGallery(BaseModel):
    title = models.CharField(blank=True, null=True, max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    photo = models.ImageField(upload_to='photo')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     options={'quality': 85})
    gallery = models.ForeignKey(PhotoGallery)
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from djanao.models import BaseModel


class Detail(BaseModel):
    heading = models.CharField(max_length=128, blank=True)
    image = ProcessedImageField(upload_to='detail', processors=[ResizeToFill(800, 400)], blank=True)
    text = RichTextUploadingField()

    def __str__(self):
        return self.heading or self.text[:30]

    DIRECTIVE = 'defaultView'

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import strip_tags
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill, ResizeToFit

from djanao.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=128)
    image = ProcessedImageField(upload_to='news', processors=[ResizeToFit(800, 500)], blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 400)],
                                     options={'quality': 85})
    date = models.DateTimeField(auto_now_add=True)
    announce = models.CharField(max_length=255, blank=True)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.announce:
            self.announce = strip_tags(self.text)[:255]
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ('-date',)
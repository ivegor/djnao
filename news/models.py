from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.html import strip_tags
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill, ResizeToFit

from djanao.models import BaseModel
from documents.models import Document


class News(BaseModel):
    title = models.CharField(max_length=128)
    image = ProcessedImageField(upload_to='news',
                                processors=[ResizeToFit(800, 500)],
                                null=True,
                                blank=True)
    image_thumbnail = ProcessedImageField(upload_to='news',
                                          processors=[ResizeToFill(400, 400)],
                                          options={'quality': 85},
                                          null=True,
                                          blank=True)
    date = models.DateTimeField(auto_now_add=True)
    announce = models.CharField(max_length=255, blank=True)
    text = RichTextUploadingField()
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.announce:
            self.announce = strip_tags(self.text)[:255]
        if not self.image_thumbnail and self.image:
            self.image_thumbnail.save(self.image.name, self.image)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ('-date',)


class NewsAdditional(models.Model):
    news = models.OneToOneField(News, related_name='additional')
    likes = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveSmallIntegerField(default=0)


from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from djanao.models import BaseModel


class News(BaseModel):
    title = models.CharField()
    text = RichTextUploadingField()
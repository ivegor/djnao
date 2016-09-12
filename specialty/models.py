from ckeditor.fields import RichTextField
from django.db import models

from djanao.models import BaseModel


class Speciality(BaseModel):
    title = models.CharField(max_length=127, verbose_name='название')
    qualification = models.TextField(max_length=255, verbose_name='квалификации')
    area = models.CharField(max_length=255, verbose_name='область профессиональной деятельности')
    activities = models.TextField(verbose_name='виды деятельности')
    code = models.CharField(max_length=10, verbose_name='код')

    def __str__(self):
        return self.title

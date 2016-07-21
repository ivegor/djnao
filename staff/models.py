from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from djanao.models import BaseModel


class Staff(BaseModel):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField()
    CATEGORIES =(('администрация', 'администрация'),
                 ('педагоги', 'педагог'),
                 ('обслуживающий персонал', 'обслуживающий персонал'))
    category = models.CharField(choices=CATEGORIES, max_length=64)
    image = ProcessedImageField(upload_to='detail', processors=[ResizeToFill(400, 400)], blank=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from djanao.models import BaseModel


class Staff(BaseModel):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    phone = models.PositiveSmallIntegerField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=10)
    CATEGORIES =(('администрация', 'администрация'),
                 ('педагоги', 'педагог'),
                 ('обслуживающий персонал', 'обслуживающий персонал'))
    category = models.CharField(choices=CATEGORIES, max_length=64)
    image = ProcessedImageField(upload_to='detail', processors=[ResizeToFill(240, 240)], blank=True, null=True)
    SEX =((True, 'мужской'),
          (False, 'женский'))
    sex = models.BooleanField(default=True, choices=SEX)
    text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('category', 'order')


class AdditionalInformation(models.Model):
    staff = models.OneToOneField(Staff)
    teacher_category = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=255)
    teach_exp = models.CharField(max_length=50)
    cur_exp = models.DateField()
    training = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

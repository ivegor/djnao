from django.db import models

from djanao.models import BaseModel


class Additional(models.Model):
    speciality = models.OneToOneField('specialty.Speciality', related_name='additional')
    active = models.BooleanField(default=True, verbose_name='есть в этом году')
    FORMS = (('ft', 'очная'),
             ('pt', 'заочная'),
             ('ev', 'вечерняя'))
    form_learning = models.CharField(max_length=2, choices=FORMS, verbose_name='форма обучения')
    budgets = models.PositiveSmallIntegerField(verbose_name='количество бюджетных мест')
    requests = models.PositiveSmallIntegerField(verbose_name='поданных заявлений')


class Speciality(BaseModel):
    title = models.CharField(max_length=127, verbose_name='название')
    PROFILES = (('te', 'технический'),
                ('na', 'естественно-научный'))
    profile = models.CharField(max_length=2, choices=PROFILES, verbose_name='профиль')
    qualifications = models.TextField(max_length=255, verbose_name='квалификации')
    area = models.CharField(max_length=255, verbose_name='область профессиональной деятельности')
    activities = models.TextField(verbose_name='виды деятельности')
    code = models.CharField(max_length=10, verbose_name='код')

    def __str__(self):
        return self.title

    ADDITIONAL = {'profiles': {t[0]: t[1] for t in PROFILES},
                  'forms': {t[0]: t[1] for t in Additional.FORMS}}

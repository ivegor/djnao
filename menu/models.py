from collections import namedtuple

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from mptt.models import MPTTModel, TreeForeignKey

nt = namedtuple('Obj', 'content directive many')


class TupleGenericForeignKey(GenericForeignKey):
    def __get__(self, instance, instance_type=None):
        g = super().__get__(instance, instance_type)
        if g:
            return nt(g, g.directive(), False)
        elif instance.content_type:
            model = instance.content_type.model_class()
            directive = model.directive
            return nt(model.objects.all(), directive(), True)
        else:
            return


class Menu(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, unique=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    order = models.PositiveSmallIntegerField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True, verbose_name='тип')
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = TupleGenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('order',)
        unique_together = ('order', 'parent')

    def __str__(self):
        return self.name

    def do_slug(self):
        self.slug = slugify(unidecode(self.name))



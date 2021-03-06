from collections import namedtuple

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from djanao.models import BaseModel

nt = namedtuple('Obj', 'content template many additional')


class TupleGenericForeignKey(GenericForeignKey):
    def __get__(self, instance, instance_type=None):
        g = super().__get__(instance, instance_type)
        if g:
            return nt(g, g.template_detail(), False, g.get_additional())
        elif instance.content_type:
            model = instance.content_type.model_class()
            template = model.template_list()
            additional = model.get_additional()
            return nt(model.objects.all(), template, True, additional)
        else:
            return


class AbsMenu(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True
        ordering = ('order',)

    def __str__(self):
        return self.name


class GroupMenu(AbsMenu):
    blank = models.BooleanField(default=False)


class MainMenu(AbsMenu):
    group = models.ForeignKey(GroupMenu, related_name='main_menus')

    class Meta:
        unique_together = ('group', 'order')


class SubMenu(AbsMenu):
    main_menu = models.ForeignKey(MainMenu, related_name='sub_menus')
    slug = models.SlugField(blank=True, unique=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True, verbose_name='тип')
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = TupleGenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('order',)
        unique_together = ('main_menu', 'order')

    def __str__(self):
        return self.name

    def do_slug(self):
        self.slug = slugify(unidecode(self.name))


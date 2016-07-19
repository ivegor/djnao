from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    order = models.PositiveSmallIntegerField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    object_id = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('order',)
        unique_together = ('order', 'parent')

    def __str__(self):
        return self.name

    def do_slug(self):
        self.slug = slugify(unidecode(self.name))

from django.db import models

from djanao.models import BaseModel


class Document(BaseModel):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.title:
            self.title = self.file.name
        super().save(force_insert, force_update, using, update_fields)

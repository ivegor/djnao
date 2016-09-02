from django.db import models


class BaseModel(models.Model):

    @classmethod
    def template(cls):
        return cls.TEMPLATE if hasattr(cls, 'TEMPLATE') else cls.__name__.lower()

    class Meta:
        abstract = True

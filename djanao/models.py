from django.db import models


class BaseModel(models.Model):

    @classmethod
    def directive(cls):
        return cls.DIRECTIVE if hasattr(cls, 'DIRECTIVE') else cls.__name__.lower()

    class Meta:
        abstract = True

from django.db import models


class BaseModel(models.Model):

    @classmethod
    def template_list(cls):
        return cls.TEMPLATE_LIST if hasattr(cls, 'TEMPLATE_LIST') else cls.__name__.lower() + '_list'

    @classmethod
    def template_detail(cls):
        return cls.TEMPLATE_DETAIL if hasattr(cls, 'TEMPLATE_DETAIL') else cls.__name__.lower() + '_detail'

    class Meta:
        abstract = True

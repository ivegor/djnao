from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm

from admin.widgets import ChoiceGenericForeignKey
from djanao.models import BaseModel
from menu.models import Menu


class MenuForm(ModelForm):
    content_type = forms.ChoiceField(choices=lambda: ((model.id, model.model) for model in ContentType.objects.all()
                                                      if model and issubclass(model.model_class(), BaseModel)))
    object_id = forms.IntegerField(widget=ChoiceGenericForeignKey())

    class Meta:
        model = Menu
        fields = '__all__'


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)
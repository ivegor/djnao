from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm

from django_mptt_admin.admin import DjangoMpttAdmin

from admin.widgets import ChoiceGenericForeignKey, LeftRight
from menu.models import Menu


class MenuForm(ModelForm):
    order = forms.ChoiceField(choices=((x, x) for x in range(1, 11)), widget=LeftRight())
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(app_label__in=('detail', 'staff', 'blocks')))
    object_id = forms.IntegerField(widget=ChoiceGenericForeignKey())

    class Meta:
        model = Menu
        fields = '__all__'


class MenuAdmin(DjangoMpttAdmin):
    form = MenuForm

admin.site.register(Menu, MenuAdmin)
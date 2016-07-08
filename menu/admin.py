from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm

from admin.widgets import ChoiceGenericForeignKey
from menu.models import Menu


class MenuForm(ModelForm):
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(app_label__in=('detail', 'staff', 'blocks')))
    object_id = forms.IntegerField(widget=ChoiceGenericForeignKey())

    class Meta:
        model = Menu
        fields = '__all__'


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)
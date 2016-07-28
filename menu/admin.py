from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.forms import ModelForm

from django_mptt_admin.admin import DjangoMpttAdmin

from admin.views import ajax_admin_update
from admin.widgets import ChoiceGenericForeignKey, LeftRight
from menu.models import Menu, SubMenu, MainMenu, GroupMenu


class MenuForm(ModelForm):
    order = forms.IntegerField(widget=LeftRight())
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(app_label__in=('detail', 'staff', 'blocks')), required=False)
    object_id = forms.IntegerField(widget=ChoiceGenericForeignKey(), required=False)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuAdmin(DjangoMpttAdmin):
    form = MenuForm

    def get_urls(self):
        return [
           url(r'^ajax/(?P<id>\d+)$', ajax_admin_update, name='ajax_admin_update')
        ] + super(MenuAdmin, self).get_urls()


class SubMenuForm(ModelForm):
    order = forms.IntegerField(widget=LeftRight())
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(app_label__in=('detail', 'staff', 'blocks')), required=False)
    object_id = forms.IntegerField(widget=ChoiceGenericForeignKey(), required=False)

    class Meta:
        model = SubMenu
        fields = '__all__'


class SubMenuAdmin(admin.ModelAdmin):
    form = SubMenuForm

    def get_urls(self):
        return [
           url(r'^ajax/(?P<id>\d+)$', ajax_admin_update, name='ajax_admin_update')
        ] + super(SubMenuAdmin, self).get_urls()


admin.site.register(Menu, MenuAdmin)
admin.site.register(GroupMenu)
admin.site.register(MainMenu)
admin.site.register(SubMenu, SubMenuAdmin)

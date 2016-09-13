from django.contrib import admin

from specialty.models import Speciality, Additional


class AdditionalInline(admin.TabularInline):
    model = Additional


class SpecialityAdmin(admin.ModelAdmin):
    inlines = [
        AdditionalInline,
    ]

admin.site.register(Speciality, SpecialityAdmin)

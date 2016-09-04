from django.contrib import admin
from staff.models import Staff, AdditionalInformation


class AdditionalInline(admin.TabularInline):
    model = AdditionalInformation


class StaffAdmin(admin.ModelAdmin):
    inlines = [
        AdditionalInline,
    ]


admin.site.register(Staff, StaffAdmin)
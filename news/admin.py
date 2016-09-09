from django.contrib import admin
from imagekit.admin import AdminThumbnail

from documents.models import Document
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumbnail')


admin.site.register(News, NewsAdmin)

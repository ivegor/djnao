from django.contrib import admin
from gallery.models import PhotoGallery, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(PhotoGallery, GalleryAdmin)

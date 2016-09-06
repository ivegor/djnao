from rest_framework import serializers

from gallery.models import PhotoGallery


class GalleriesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.photo_set.first().photo_thumbnail.url


    class Meta:
        model = PhotoGallery

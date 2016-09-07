from rest_framework import serializers

from gallery.models import PhotoGallery, Photo


class GalleriesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.photo_set.first().photo_thumbnail.url

    class Meta:
        model = PhotoGallery


class _PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.photo.url

    def get_thumbnail(self, obj):
        return obj.photo_thumbnail.url

    class Meta:
        model = Photo
        fields = ('id', 'title', 'photo', 'thumbnail')


class GallerySerializer(serializers.ModelSerializer):
    photo_set = _PhotoSerializer(many=True)

    class Meta:
        model = PhotoGallery
        fields = ('title', 'photo_set')

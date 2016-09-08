from rest_framework import serializers

from news.models import News


class GalleriesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj

    class Meta:
        model = News


class NewsListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.image_thumbnail.url

    class Meta:
        model = News
        fields = ('id', 'title', 'thumbnail', 'announce')

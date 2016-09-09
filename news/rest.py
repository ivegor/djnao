from rest_framework import serializers

from news.models import News


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'date', 'image', 'text')


class NewsListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.image_thumbnail.url

    class Meta:
        model = News
        fields = ('id', 'title', 'date',  'thumbnail', 'announce')

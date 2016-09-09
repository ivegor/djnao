from rest_framework import serializers

from news.models import News
from news.signals import add_views


class NewsDetailSerializer(serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    additional = serializers.SerializerMethodField()

    def get_documents(self, obj):
        return tuple({'title': i.title, 'url': i.file.url} for i in obj.documents.all())

    def get_additional(self, obj):
        views, likes = add_views(obj)
        return {'views': views, 'likes': likes}

    class Meta:
        model = News
        fields = ('id', 'title', 'date', 'image', 'text', 'documents', 'additional')


class NewsListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.image_thumbnail.url if obj.image_thumbnail else ''

    class Meta:
        model = News
        fields = ('id', 'title', 'date',  'thumbnail', 'announce')

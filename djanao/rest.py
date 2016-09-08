from collections import UserDict

from rest_framework import serializers

from documents.rest import DocumentSerializer
from gallery.rest import GalleriesSerializer, GallerySerializer
from news.rest import NewsListSerializer
from staff.rest import StaffSerializer


class DefaultSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {k: v for k, v in instance.__dict__.items() if not k.startswith('_')}


class DictWithDefault(UserDict):
    def __missing__(self, key):
        return DefaultSerializer


SERIALIZERS = DictWithDefault({
    'staff_list': StaffSerializer,
    'document_list': DocumentSerializer,
    'photogallery_list': GalleriesSerializer,
    'photogallery_detail': GallerySerializer,
    'news_list': NewsListSerializer
})

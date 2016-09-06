from collections import UserDict

from rest_framework import serializers

from documents.rest import DocumentSerializer
from gallery.rest import GalleriesSerializer
from staff.rest import StaffSerializer


class DefaultSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {k: v for k, v in instance.__dict__.items() if not k.startswith('_')}


class DictWithDefault(UserDict):
    def __missing__(self, key):
        return DefaultSerializer


SERIALIZERS = DictWithDefault({
    'staff': StaffSerializer,
    'document': DocumentSerializer,
    'photogallery': GalleriesSerializer
})

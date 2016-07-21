from collections import UserDict

from rest_framework import serializers


class DefaultSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {k: v for k, v in instance.__dict__.items() if not k.startswith('_')}


class DictWithDefault(UserDict):
    def __missing__(self, key):
        return DefaultSerializer


SERIALIZERS = DictWithDefault({

})

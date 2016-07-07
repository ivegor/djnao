from rest_framework import serializers


class AjaxAdminSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        for x in 'name', 'heading', 'title':
            if hasattr(obj, x):
                return getattr(obj, x)


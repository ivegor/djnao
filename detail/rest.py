from rest_framework import serializers

from detail.models import Detail


class DetailSerializer(serializers.ModelSerializer):
    heading = serializers.SerializerMethodField('heading_or_menu')

    def heading_or_menu(self, obj):
        return obj.heading or obj.menu.name

    class Meta:
        model = Detail
        fields = ('heading', 'image', 'text')

from rest_framework import serializers

from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    side = serializers.SerializerMethodField()

    def get_side(self, obj):
        return 'right' if obj.order >= 100 else 'left'

    class Meta:
        model = Menu
        fields = ('slug', 'name', 'order', 'side')

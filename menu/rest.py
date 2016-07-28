from rest_framework import serializers

from menu.models import Menu, GroupMenu, MainMenu, SubMenu


class _MenuSerializer(serializers.ModelSerializer):
    side = serializers.SerializerMethodField()

    def get_side(self, obj):
        return 'right' if obj.order >= 100 else 'left'

    class Meta:
        model = Menu
        fields = ('slug', 'name', 'order', 'side')


class _SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = ('name', 'slug')


class _MainMenuSerializer(serializers.ModelSerializer):
    sub_menus = _SubMenuSerializer(many=True)

    class Meta:
        model = MainMenu
        fields = ('name', 'sub_menus')


class MenuSerializer(serializers.ModelSerializer):
    main_menus = _MainMenuSerializer(many=True)
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name if not obj.blank else None

    class Meta:
        model = GroupMenu
        fields = ('name', 'main_menus')

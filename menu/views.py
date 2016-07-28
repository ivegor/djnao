from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from djanao.rest import SERIALIZERS
from menu import rest
from menu.models import Menu, GroupMenu


def _menu(request, path=None):
    data = {}
    if not path:
        menus = Menu.objects.filter(parent_id__isnull=True)
    else:
        current_menu = get_object_or_404(Menu, slug=path)
        model = current_menu.content_object
        menus = current_menu.get_children()
        if model:
            data['content'] = SERIALIZERS[model.directive](model.content, many=model.many).data
            data['directive'] = model.directive

    data['menu'] = rest.MenuSerializer(menus, many=True).data
    print(data)
    return JsonResponse(data, safe=False)


def menu(request, path=None):
    data = rest.MenuSerializer(GroupMenu.objects.all(), many=True).data
    print(data)
    return JsonResponse(data, safe=False)

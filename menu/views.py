from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from menu import rest
from menu.models import Menu
from staff.rest import StaffSerializer


def menu(request, path=None):
    if not path:
        menu_objs = Menu.objects.filter(parent_id__isnull=True)
        model = (None, None)
    else:
        current_menu = get_object_or_404(Menu, slug=path)
        model = current_menu.content_object
        menu_objs = current_menu.get_children()
    js = rest.MenuSerializer(menu_objs, many=True)
    if model[0]:
        content = StaffSerializer(model[0], many=model[2])
    return JsonResponse({
                        'menu': js.data,
                        'directive': model[1],
                        'content': content.data if model[0] else model
                        }, safe=False)

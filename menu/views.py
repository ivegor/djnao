from django.http import JsonResponse

from menu import rest
from menu.models import Menu


def menu(request, path=None):
    if not path:
        menu_obj = Menu.objects.filter(parent_id__isnull=True)
    else:
        menu_obj = Menu.objects.filter(parent__slug=path)
    js = rest.MenuSerializer(menu_obj, many=True)
    return JsonResponse(js.data, safe=False)
from django.http import JsonResponse

from menu import rest
from menu.models import GroupMenu


def menu(request, path=None):
    data = rest.MenuSerializer(GroupMenu.objects.all(), many=True).data
    print(data)
    return JsonResponse(data, safe=False)

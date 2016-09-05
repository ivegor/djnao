from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from base import rest
from base.models import Base
from djanao.rest import SERIALIZERS
from menu.models import SubMenu


def base(request):
    base_obj = Base.objects.first()
    js = rest.BaseSerializer(base_obj)
    return JsonResponse(js.data)


def app(request, path):
    data = {}
    current_menu = get_object_or_404(SubMenu, slug=path)
    model = current_menu.content_object
    if model:
        data['content'] = SERIALIZERS[model.template](model.content, many=model.many).data
        data['template'] = model.template

    print(data)
    return JsonResponse(data, safe=False)

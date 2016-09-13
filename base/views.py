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


def app(request, slug, id=None):
    data = {}
    current_menu = get_object_or_404(SubMenu, slug=slug)
    if id:
        current_menu.object_id = id
    model = current_menu.content_object
    data['content'] = SERIALIZERS[model.template](model.content, many=model.many).data
    data['template'] = model.template
    if model.additional:
        data['additional'] = model.additional
    return JsonResponse(data, safe=False)


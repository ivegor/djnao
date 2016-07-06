from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from detail import rest
from detail.models import Detail


def detail(request, slug):
    detail_obj = get_object_or_404(Detail, menu__slug=slug)
    js = rest.DetailSerializer(detail_obj)
    return JsonResponse(js.data)
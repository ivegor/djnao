from django.http import JsonResponse

from base import rest
from base.models import Base


def base(request):
    base_obj = Base.objects.first()
    js = rest.BaseSerializer(base_obj)
    return JsonResponse(js.data)

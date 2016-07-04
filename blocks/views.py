from django.http import JsonResponse

from blocks import rest
from blocks.models import Slider


def slider(request):
    base_obj = Slider.objects.all()
    js = rest.SliderSerializer(base_obj, many=True)
    return JsonResponse(js.data, safe=False)
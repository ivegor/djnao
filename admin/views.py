from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse

from admin.rest import AjaxAdminSerializer


def ajax_admin_update(request, id):
    model = ContentType.objects.get(id=id)
    objects = model.model_class().objects.all()
    js = AjaxAdminSerializer(objects, many=True)
    return JsonResponse(js.data, safe=False)


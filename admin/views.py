from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse

from admin.rest import AjaxAdminSerializer


@login_required
def ajax_admin_update(request, id):
    model = ContentType.objects.get(id=id)
    objects = model.model_class().objects.all()
    js = AjaxAdminSerializer(objects, many=True)
    return JsonResponse(js.data, safe=False)


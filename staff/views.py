import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from staff.models import Staff


@api_view(['POST'])
def like(request):
    data = request.data
    id = data.get('id')
    st = Staff.objects.get(id=id)
    st.additionalinformation.likes += 1
    st.additionalinformation.save()
    return Response(status=201)


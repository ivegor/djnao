from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News


@api_view(['POST'])
def news_like(request):
    data = request.data
    id = data.get('id')
    st = News.objects.get(id=id)
    st.additional.likes += 1
    st.additional.save()
    return Response(status=201)
from news.models import NewsAdditional


def add_views(instance):
    additional = NewsAdditional.objects.get_or_create(news=instance)[0]
    additional.views += 1
    additional.save()
    return additional.views, additional.likes


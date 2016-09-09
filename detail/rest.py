from rest_framework import serializers

from detail.models import Detail


class DetailSerializer(serializers.ModelSerializer):
    heading = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    documents = serializers.SerializerMethodField()

    def get_documents(self, obj):
        return tuple({'title': i.title, 'url': i.file.url} for i in obj.documents.all())

    def get_heading(self, obj):
        return obj.heading or obj.menu.name

    def get_image(self, obj):
        return obj.image.url if obj.image else ''

    class Meta:
        model = Detail
        fields = ('heading', 'image', 'text')

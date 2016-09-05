from rest_framework import serializers

from documents.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    mime_type = serializers.SerializerMethodField()

    def get_file(self, obj):
        return obj.file.url

    def get_size(self, obj):
        return '%s мб' % (round(obj.file.size/1024/1024, 2))

    def get_mime_type(self, obj):
        spl = obj.file.name.split('.')
        return spl[-1] if len(spl) > 1 else ''

    class Meta:
        model = Document

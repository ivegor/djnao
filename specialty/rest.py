from rest_framework import serializers

from specialty.models import Speciality, Additional


class _SpecialityAdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        exclude = ('id',)


class SpecialityListSerializer(serializers.ModelSerializer):
    qualifications = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()
    additional = _SpecialityAdditionalSerializer()

    def get_qualifications(self, obj):
        return [q for q in obj.qualifications.split('\n') if not q.isspace()]

    def get_activities(self, obj):
        return [a for a in obj.activities.split('\n') if not a.isspace()]

    class Meta:
        model = Speciality
        fields = ('title', 'qualifications', 'area', 'activities', 'code', 'profile', 'additional')


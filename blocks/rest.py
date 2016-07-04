from rest_framework import serializers

from blocks.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

from rest_framework.serializers import ModelSerializer

from material.models import Сourse


class СourseSerializer(ModelSerializer):
    class Meta:
        model = Сourse
        fields = "__all__"

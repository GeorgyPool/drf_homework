from rest_framework import viewsets

from material.models import Сourse
from material.serializers import СourseSerializer


class СourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializer
    queryset = Сourse.objects.all()

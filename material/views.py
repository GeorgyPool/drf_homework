from rest_framework import generics, viewsets

from material.models import Lesson, Course
from material.serializers import LessonSerializer, CourseSerializer

"""
Представление для Сourse API endpoint в формате ViewSet
"""


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


"""
Представления для класса Lesson API endpoint в формате CRUD generics
"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonReadAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIVIew(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

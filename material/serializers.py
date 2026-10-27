from rest_framework.serializers import ModelSerializer, SerializerMethodField

from material.models import Lesson, Course


class CourseSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lesson(self, instance):
        return instance.lesson.count()


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

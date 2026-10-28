from rest_framework.serializers import ModelSerializer, SerializerMethodField

from material.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lesson(self, instance):
        return instance.lesson.count()

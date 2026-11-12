from rest_framework.serializers import ModelSerializer, SerializerMethodField

from material.models import Course, Lesson
from material.validators import CheckingUrl


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [CheckingUrl(field="url_video")]


class CourseSerializer(ModelSerializer):
    # считает количество уроков для каждого курса
    count_lesson = SerializerMethodField()
    # выводит информацию об уроках для каждого курса
    lesson = LessonSerializer(many=True, read_only=True)
    # выводит список email всех пользователей подписанных на конкретный курс
    subscribers = SerializerMethodField()
    # проверяет есть ли у текущего пользователя подписка на конкретный курс
    is_your_subscribe = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lesson(self, instance):
        return instance.lesson.count()

    def get_subscribers(self, instance):
        return [sub.user.email for sub in instance.sub_course.all()]

    def get_is_your_subscribe(self, instance):

        request = self.context.get("request", None)
        if not request or not request.user.is_authenticated:
            return False

        is_subscribe = instance.sub_course.filter(user=request.user).exists()
        return True if is_subscribe else False

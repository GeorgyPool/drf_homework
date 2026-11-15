from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from material.models import Course, Lesson
from material.paginations import CourseListPaginator, LessonListPaginator
from material.serializers import CourseSerializer, LessonSerializer
from material.tasks import send_message_for_update_material_course
from users.models import Subscription
from users.permissions import IsModer, IsOwner

"""
Представление для Сourse API endpoint в формате ViewSet
"""


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CourseListPaginator

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, ~IsModer, IsOwner]
        elif self.action == "update":
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]

        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


"""
Представления для класса Lesson API endpoint в формате CRUD generics
"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

        # при добавлении нового урока в курс,
        # при наличии у пользователя подписки на данный курс ему отправляется сообщение на почту о новом уроке
        send_message_for_update_material_course.delay(lesson.course_id, lesson.title)


class LessonReadAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonListPaginator
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDeleteAPIVIew(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

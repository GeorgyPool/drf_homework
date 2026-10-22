from django.urls import path
from rest_framework.routers import DefaultRouter

from material.apps import MaterialConfig

from . import views

app_name = MaterialConfig.name
router = DefaultRouter()
router.register(r"course", views.СourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", views.LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lesson/read/list/", views.LessonReadAPIView.as_view(), name="lesson_read_list"
    ),
    path(
        "lesson/read/retrieve/<int:pk>/",
        views.LessonRetrieveAPIView.as_view(),
        name="lesson_read_retrieve",
    ),
    path(
        "lesson/update/<int:pk>/",
        views.LessonUpdateAPIView.as_view(),
        name="lesson_update",
    ),
    path(
        "lesson/delete/<int:pk>/",
        views.LessonDeleteAPIVIew.as_view(),
        name="lesson_delete",
    ),
] + router.urls

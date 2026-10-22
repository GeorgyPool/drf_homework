from django.urls import path
from rest_framework.routers import DefaultRouter

from material.apps import MaterialConfig

from . import views

app_name = MaterialConfig.name
router = DefaultRouter()
router.register(r"course", views.СourseViewSet, basename="course")

urlpatterns = [] + router.urls

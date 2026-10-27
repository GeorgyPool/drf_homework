from django.urls import path

from home.apps import HomeConfig

from . import views

app_name = HomeConfig.name

urlpatterns = [path("", views.HomeTemplateView.as_view(), name="home")]

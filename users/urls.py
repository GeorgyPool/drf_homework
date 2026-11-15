from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"options", views.UserViewSet, basename="options")
router.register(r"subscriptions", views.UserSubscriptions, basename="subscriptions")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="register"),
    path("refresh/token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("payment/list/", views.PaymentAPIList.as_view(), name="payment_list"),
    path("payment/create/", views.PaymentAPICreate.as_view(), name="payment_create"),
] + router.urls

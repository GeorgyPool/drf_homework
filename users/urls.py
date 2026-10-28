from django.urls import path

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

urlpatterns = [
    path("payment/list/", views.PaymentAPIList.as_view(), name="payment_list")
]

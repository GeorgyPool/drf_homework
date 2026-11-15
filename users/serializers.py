from rest_framework import serializers

from users.models import Payment, Subscription, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["course", "lesson", "payment_method", "session_id", "link_payment"]
        extra_kwargs = {
            "session_id": {"read_only": True},
            "link_payment": {"read_only": True},
        }


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ["user"]
        extra_kwargs = {"user": {"read_only": True}}

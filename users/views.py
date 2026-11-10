from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import Payment, Subscription, User
from users.permissions import IsModer, IsUser, IsOwnerSubscribe
from users.serializers import (PaymentSerializer, SubscriptionSerializer,
                               UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action == "list":
            self.permission_classes = [IsModer]
        elif self.action in ["retrieve", "update", "destroy"]:
            self.permission_classes = [IsUser]
            pass

        return super().get_permissions()


class PaymentAPIList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["course_id", "lesson_id"]
    search_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["price", "created_at"]


class UserSubscriptions(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "destroy":
            self.permission_classes = [IsOwnerSubscribe]
        return super().get_permissions()

    def perform_create(self, serializer):

        user = self.request.user
        course = serializer.validated_data["course"]

        if Subscription.objects.filter(user=user, course=course).exists():
            raise ValidationError("Эта подписка у вас уже есть")
        else:
            serializer.save(user=user)

    def perform_destroy(self, instance):

        user = self.request.user
        if instance.user == user:
            instance.delete()

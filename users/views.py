from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentAPIList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["course_id", "lesson_id"]
    search_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["price", "created_at"]

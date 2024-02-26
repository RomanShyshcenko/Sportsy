from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

from core.permissions import IsAuthenticatedAuthor
from subscription import serializers
from subscription.models import Subscription

User = get_user_model()


class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = serializers.SubscriptionSerializer
    permission_classes = [IsAuthenticatedAuthor]
    authentication_classes = [JWTAuthentication]


class SubscriptionRetrieveUpdateAPIView(RetrieveAPIView):
    serializer_class = serializers.SubscriptionSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_object(self):
        pk = self.request.query_params.get('pk')
        subscription = get_object_or_404(Subscription, pk=pk)
        return subscription

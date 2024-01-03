from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from user import serializers
from user.services.email_service import EmailService
from user.services.get_user import GetUserService
from user.services.update_api_view import CustomUpdateAPIView


User = get_user_model()


class RegisterUserAPIView(CreateAPIView):
    """Create User with email and password field"""
    serializer_class = serializers.RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)


class RetrieveUserAPIView(RetrieveAPIView):
    """Retrieve User by JWT Authentication"""
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        """Get user"""
        user_uuid = self.request.user.uuid
        return GetUserService.get_user_by_uuid(user_uuid=user_uuid)


class UpdateUserAPIView(CustomUpdateAPIView):
    """Create or update user first_name, last_name and address fields"""
    serializer_class = serializers.UserSerializer


class ChangePasswordAPIView(CustomUpdateAPIView):
    """Change User password"""
    serializer_class = serializers.ChangePasswordSerializer


class ChangeEmailAPIView(CustomUpdateAPIView):
    """Change User email with setting is_confirmed_email to False"""
    serializer_class = serializers.ChangeEmaiSerializer


class SendEmailVerification(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = self.request.user
        return EmailService.send_activation_email(user)


class EmailVerification(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user_id = self.request.query_params.get('user_id', '')
        confirmation_token = self.request.query_params.get('confirmation_token', '')
        return EmailService.verify_email(user_id, confirmation_token)

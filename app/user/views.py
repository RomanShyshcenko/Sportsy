from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from app.user import serializers
from app.user.services.get_user import GetUserService
from app.user.services.update_api_view import CustomUpdateAPIView


# Create your views here.

class RegisterUserAPIView(CreateAPIView):
    """Create User with email and password field"""
    serializer_class = serializers.RegisterUserSerializer
    authentication_classes = ()


class RetrieveUserAPIView(RetrieveAPIView):
    """Retrieve User by JWT Authentication"""
    authentication_classes = (JSONWebTokenAuthentication,)
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

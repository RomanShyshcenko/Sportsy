from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework import permissions
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
from user.tasks import send_verify_email, send_reset_password_email
from django.contrib.auth import logout

User = get_user_model()


def logout_user_view(request):
    logout(request)
    return redirect(reverse('user:create'))


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
        user_uuid = self.request.user.id
        return GetUserService.get_user_by_uuid(user_uuid=user_uuid)


class UpdateUserAPIView(CustomUpdateAPIView):
    """Create or update user first_name, last_name and address fields"""
    serializer_class = serializers.UserSerializer


class ChangePasswordAPIView(CustomUpdateAPIView):
    """Change User password"""
    serializer_class = serializers.ChangePasswordSerializer


class ResetPasswordAPIView(CustomUpdateAPIView):
    """Reset user password"""
    serializer_class = serializers.ChangeForgottenPasswordSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get_object(self) -> User:
        user_id = self.request.query_params.get('user_id', '')
        return get_object_or_404(User, id=user_id)

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        reset_token = self.request.query_params.get('reset_token', '')
        serializer = self.get_serializer(instance, data=request.data)

        if not default_token_generator.check_token(instance, reset_token):
            return Response('Token is invalid or expired. Please request another.', status=400)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Updated successes"})

        return Response({"message": "failed", "details": serializer.errors})


class SendResetPasswordEmailAPIView(APIView):
    """Sends reset password email"""
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data['email']
        get_object_or_404(User, email=email)
        send_reset_password_email.delay(email)
        return Response(status=200)


class ChangeEmailAPIView(CustomUpdateAPIView):
    """Change User email with setting is_confirmed_email to False"""
    serializer_class = serializers.ChangeEmaiSerializer


class SendEmailVerification(APIView):
    """Sends verification for email"""
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = self.request.user
        return send_verify_email(user)


class EmailVerification(APIView):
    """Verifies email"""
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user_id = self.request.query_params.get('user_id', '')
        confirmation_token = self.request.query_params.get('confirmation_token', '')
        return EmailService.verify_email(user_id, confirmation_token)

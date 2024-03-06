from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.conf import settings


User = get_user_model()


class EmailService:
    @staticmethod
    def send_activation_email(user: User):

        confirmation_token = default_token_generator.make_token(user)
        user_id = user.id
        body = f"Here is your confirmation url http://localhost:8000/{reverse('user:email_verification')}" \
               f"?user_id={user_id}&confirmation_token={confirmation_token}",

        msg = EmailMultiAlternatives(
            # title:
            "Email verification for {title}".format(title="..."),
            # message:
            body,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            [user.email],
        )
        print(body)
        try:
            if msg.send():
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def send_password_reset_email(user: User) -> bool:
        secret_token = default_token_generator.make_token(user)
        user_id = user.id
        body = (
            f"Here is your reset password url http://localhost:8000/"
            f"{reverse('user:reset_password')}"
            f"?user_id={user_id}&reset_token={secret_token}"
            )

        msg = EmailMultiAlternatives(
            # title:
            "Password Reset for {title}".format(title="..."),
            # message:
            body,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            [user.email]
        )
        print(body)
        try:
            if msg.send():
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def verify_email(user_id: int, confirmation_token: int):
        user = get_object_or_404(User, id=user_id)

        if not default_token_generator.check_token(user, confirmation_token):
            return Response('Token is invalid or expired. Please request another confirmation email by signing in.',
                            status=status.HTTP_400_BAD_REQUEST)
        if user.is_confirmed_email:
            return Response('Email has already been verified.', status=status.HTTP_400_BAD_REQUEST)

        user.activate_email()
        user.save()

        return Response('Email successfully confirmed')

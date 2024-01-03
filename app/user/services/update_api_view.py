from django.contrib.auth import get_user_model

from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


User = get_user_model()


class CustomUpdateAPIView(UpdateAPIView):
    """Updates User fields by given serializer class"""
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User

    def get_object(self) -> User:
        return self.request.user

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Updated successes"})

        return Response({"message": "failed", "details": serializer.errors})

from rest_framework.permissions import BasePermission


class IsAuthenticatedAuthor(BasePermission):
    """
    Allows access only to authenticated authors.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_author)

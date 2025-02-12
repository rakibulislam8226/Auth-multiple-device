from rest_framework.permissions import BasePermission


class IsUnauthenticated(BasePermission):
    """
    Allows access only to unauthenticated (anonymous) users.
    """

    def has_permission(self, request, view):
        return not request.user or request.user.is_anonymous

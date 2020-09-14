from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # check if valid token has been provided
        try:
            return request.user.is_authenticated
        except AttributeError:
            return False

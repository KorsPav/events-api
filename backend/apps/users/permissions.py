from rest_framework.permissions import BasePermission


class IsProfileOwner(BasePermission):
    """
    Allows access only to own profile
    """
    message = "You don`t have permission to access other users' profiles"

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id

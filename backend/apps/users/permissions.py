from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProfileOwner(BasePermission):
    message = "You don`t have permission to other users' profiles"

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id

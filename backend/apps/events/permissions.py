from rest_framework.permissions import BasePermission


class IsEventCreator(BasePermission):
    """
    Allows access only for the creator
    """

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user

from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from . import serializers, permissions

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet,):
    serializer_class = serializers.UserInfoSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'patch']
    permission_classes = (
        IsAuthenticated,
        permissions.IsProfileOwner,
    )

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

from . import serializers, services
from .permissions import IsEventCreator
from .models import Event

User = get_user_model()


class EventViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch', 'post', 'delete']

    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    filterset_fields = {
        'date': ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ('title', )

    read_permissions = (AllowAny, )
    create_permissions = (IsAuthenticated, )
    edit_permissions = (IsAuthenticated, IsEventCreator)
    registration_permissions = (IsAuthenticated, )

    permission_classes = {
        'create': create_permissions,
        'list': read_permissions,
        'retrieve': read_permissions,
        'destroy': edit_permissions,
        'partial_update': edit_permissions,
        'register': registration_permissions,
    }

    serializer_classes = {
        'create': serializers.EventCreateSerializer,
        'list': serializers.EventListSerializer,
        'retrieve': serializers.EventDetailSerializer,
        'partial_update': serializers.EventDetailSerializer,
        'register': serializers.EventRegisterSerializers,
    }

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires based on action.
        """
        permissions = self.permission_classes.get(self.action)
        return [permission() for permission in permissions]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Event.objects.all().select_related('creator')
        return Event.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    @action(
        detail=True,
        methods=['post'],
        url_path='register'
    )
    def register(self, request, *args, **kwargs):
        event = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'event': event, 'request': request})
        serializer.is_valid(raise_exception=True)
        services.register_to_event(request.user, event)
        return Response({'detail': 'Success'})

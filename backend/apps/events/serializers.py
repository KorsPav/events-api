from rest_framework import serializers

from apps.users.serializers import UserInfoSerializer
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'date',
            'created_at',
        )


class EventDetailSerializer(serializers.ModelSerializer):
    creator = UserInfoSerializer()
    participants = UserInfoSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'date',
            'location',
            'organizer',
            'created_at',
            'updated_at',
            'creator',
            'participants',
        )
        read_only_fields = (
            'id',
            'creator',
            'participants',
            'created_at',
            'updated_at',
        )


class EventCreateSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'date',
            'location',
            'organizer',
            'creator',
        )


class EventRegisterSerializers(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        user = attrs.get('user')
        event = self.context.get('event')

        if user.events.filter(id=event.id).exists():
            raise serializers.ValidationError('Already registered')

        return attrs

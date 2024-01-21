from rest_framework import serializers
from dj_rest_auth.serializers import TokenSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email'
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserInfoSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')

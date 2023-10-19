from rest_framework import serializers
from authorization.models import Permission, User
from education.models import Room
from django.core.validators import MinValueValidator, MaxValueValidator


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, max_length=150)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    permission_id = serializers.IntegerField(
        required=True,
        help_text="ID of user's permission.\n \
            Get enum on 'api/auth/permissions/'"
    )


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False, max_length=150)
    password = serializers.CharField(required=False, max_length=150)
    first_name = serializers.CharField(required=False, max_length=150)
    last_name = serializers.CharField(required=False, max_length=150)
    permission_id = serializers.IntegerField(
        required=False,
        help_text="ID of user's permission.\n \
            Get enum on 'api/auth/permissions/'"
    )


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 
                  'first_name', 'last_name', 'permission')


class ReadRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class CreateRoomSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        validators=[
            MinValueValidator(100),
            MaxValueValidator(999)
        ]
    )
    capacity = serializers.IntegerField(validators=[MinValueValidator(1)])
    description = serializers.CharField(required=False)


class UpdateRoomSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        validators=[
            MinValueValidator(100),
            MaxValueValidator(999)
        ],
        required=False
    )
    capacity = serializers.IntegerField(
        validators=[MinValueValidator(1)],
        required=False
    )
    description = serializers.CharField(required=False)
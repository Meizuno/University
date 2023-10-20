from rest_framework import serializers
from authorization.models import Permission, User
from education.models import Room, Subject
from django.core.validators import MinValueValidator, MaxValueValidator


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    permission_id = serializers.IntegerField(
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
        validators=[MinValueValidator(100), MaxValueValidator(999)]
    )
    capacity = serializers.IntegerField(validators=[MinValueValidator(1)])
    description = serializers.CharField(required=False)


class UpdateRoomSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(999)],
        required=False
    )
    capacity = serializers.IntegerField(
        validators=[MinValueValidator(1)],
        required=False
    )
    description = serializers.CharField(required=False)
    
    
class ReadSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class CreateSubjectSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=20)
    language = serializers.CharField(required=False, max_length=2)
    credits = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    capacity = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)]
    )
    guarantor_id = serializers.IntegerField()
    description = serializers.CharField(required=False)


class UpdateSubjectSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, max_length=3)
    name = serializers.CharField(required=False, max_length=20)
    language = serializers.CharField(required=False, max_length=2)
    creaits = serializers.IntegerField(
        required=False,
        validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    capacity = serializers.IntegerField(
        required=False,
        validators=[MinValueValidator(1), MaxValueValidator(9999)]
    )
    guarantor_id = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    
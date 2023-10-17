from rest_framework import serializers
from authorization.decorators import handle_error
from authorization.models import Permission, User


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserSerializator(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True, max_length=150)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    permission_id = serializers.IntegerField(
        required=True,
        help_text="ID of user's permission.\n Get enum on 'api/auth/permissions/'"
    )

    @handle_error
    def create(self, validated_data):
        return User.objects.create(**validated_data)

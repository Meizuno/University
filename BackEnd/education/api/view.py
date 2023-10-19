from rest_framework.response import Response
from rest_framework.decorators import api_view
from education.api.serializators import (
    PermissionSerializer, 
    CreateUserSerializer,
    UpdateUserSerializer,
    ReadUserSerializer,
)
from authorization.models import Permission, User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


@swagger_auto_schema(
    method='get',
    responses={
        200: PermissionSerializer(many=True),
    }
)
@api_view(['GET'])
def get_permissions(request):
    """Get all permission levels"""

    permissions = Permission.objects.all()
    serializator = PermissionSerializer(permissions, many=True)
    return Response({"data": serializator.data})


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadUserSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='post',
    request_body=CreateUserSerializer,
)
@api_view(['GET', 'POST'])
def get_users_or_create(request):
    """Read users or create new"""

    if request.method == 'GET':
        users = User.objects.all()
        serializator = ReadUserSerializer(users, many=True)
        return Response({"data": serializator.data})
    elif request.method == 'POST':
        serializator = CreateUserSerializer(data=request.data)
    if serializator.is_valid():
        User.objects.create_user(**serializator.data)
        return Response({"success": True, "errors": None})
    else:
        return Response({"success": False, "errors": serializator.errors},
                        status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadUserSerializer,
    }
)
@swagger_auto_schema(
    method='put',
    request_body=UpdateUserSerializer,
)
@swagger_auto_schema(
    method='delete',
)
@api_view(['GET', 'PUT', 'DELETE'])
def rud_user(request, user_id):
    """Read, update or delete user"""

    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        serializator = ReadUserSerializer(user)
        return Response({"data": serializator.data})
    elif request.method == 'PUT':
        serializator = UpdateUserSerializer(data=request.data)
        if serializator.is_valid():
            User.objects.filter(id=user_id).update(**serializator.validated_data)
            return Response({"success": True})
        else:
            return Response({"errors": serializator.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        User.objects.filter(id=user_id).delete()
        return Response({"success": True})

from rest_framework.response import Response
from rest_framework.decorators import api_view
from authorization.decorators import handle_error
from education.api.serializators import (
    PermissionSerializer, 
    CreateUserSerializer,
    UpdateUserSerializer,
    ReadUserSerializer,

    ReadRoomSerializer,
    CreateRoomSerializer,
    UpdateRoomSerializer,
    
    ReadSubjectSerializer,
    CreateSubjectSerializer,
    UpdateSubjectSerializer,
)
from authorization.models import Permission, User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from education.models import Room, Subject


@swagger_auto_schema(
    method='get',
    responses={
        200: PermissionSerializer(many=True),
    }
)
@api_view(['GET'])
@handle_error
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
@handle_error
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
@handle_error
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
            return Response({"success": True, "errors": None})
        else:
            return Response({"errors": serializator.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        User.objects.filter(id=user_id).delete()
        return Response({"success": True, "errors": None})


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadRoomSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='post',
    request_body=CreateRoomSerializer,
)
@api_view(['GET', 'POST'])
@handle_error
def get_rooms_or_create(request):
    """Read rooms or create new"""

    if request.method == 'GET':
        rooms = Room.objects.all()
        serializator = ReadRoomSerializer(rooms, many=True)
        return Response({"data": serializator.data})
    elif request.method == 'POST':
        serializator = CreateRoomSerializer(data=request.data)
        if serializator.is_valid():
            Room.objects.create(**serializator.data)
            return Response({"success": True, "errors": None})
        else:
            return Response({"success": False, "errors": serializator.errors},
                            status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadRoomSerializer,
    }
)
@swagger_auto_schema(
    method='put',
    request_body=UpdateRoomSerializer,
)
@swagger_auto_schema(
    method='delete',
)
@api_view(['GET', 'PUT', 'DELETE'])
@handle_error
def rud_room(request, room_id):
    """Read, update or delete room"""

    if request.method == 'GET':
        room = Room.objects.get(id=room_id)
        serializator = ReadRoomSerializer(room)
        return Response({"data": serializator.data})
    elif request.method == 'PUT':
        serializator = UpdateRoomSerializer(data=request.data)
        if serializator.is_valid():
            Room.objects.filter(id=room_id).update(**serializator.validated_data)
            return Response({"success": True, "errors": None})
        else:
            return Response({"errors": serializator.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Room.objects.filter(id=room_id).delete()
        return Response({"success": True, "errors": None})


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadSubjectSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='post',
    request_body=CreateSubjectSerializer,
)
@api_view(['GET', 'POST'])
@handle_error
def get_subjects_or_create(request):
    """Read subjects or create new"""

    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializator = ReadSubjectSerializer(subjects, many=True)
        return Response({"data": serializator.data})
    elif request.method == 'POST':
        serializator = CreateSubjectSerializer(data=request.data)
        if serializator.is_valid():
            Subject.objects.create(**serializator.data)
            return Response({"success": True, "errors": None})
        else:
            return Response({"success": False, "errors": serializator.errors},
                            status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: ReadSubjectSerializer,
    }
)
@swagger_auto_schema(
    method='put',
    request_body=UpdateSubjectSerializer,
)
@swagger_auto_schema(
    method='delete',
)
@api_view(['GET', 'PUT', 'DELETE'])
@handle_error
def rud_subject(request, subject_id):
    """Read, update or delete subject"""

    if request.method == 'GET':
        subject = Subject.objects.get(id=subject_id)
        serializator = ReadSubjectSerializer(subject)
        return Response({"data": serializator.data})
    elif request.method == 'PUT':
        serializator = UpdateSubjectSerializer(data=request.data)
        if serializator.is_valid():
            Subject.objects.filter(id=subject_id).update(**serializator.validated_data)
            return Response({"success": True, "errors": None})
        else:
            return Response({"errors": serializator.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Subject.objects.filter(id=subject_id).delete()
        return Response({"success": True, "errors": None})
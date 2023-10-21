from rest_framework.response import Response
from rest_framework.decorators import api_view
from authorization.decorators import handle_error
from authorization.models import Permission, User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from education.models import *
from education.api.serializators import *
from education.api.doc_responses import *


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_PERMISSION,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@api_view(["GET"])
@handle_error
def get_permissions(request):
    """Get all permission levels"""

    permissions = Permission.objects.all()
    serializator = PermissionSerializer(permissions, many=True)
    return Response({"data": serializator.data})


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_USER,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="post",
    request_body=CreateUserSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_DEFAULT,
    },
)
@api_view(["GET", "POST"])
@handle_error
def get_users_or_create(request):
    """Read users or create new"""

    if request.method == "GET":
        users = User.objects.all()
        serializator = ReadUserSerializer(users, many=True)
        return Response({"data": serializator.data})
    elif request.method == "POST":
        serializator = CreateUserSerializer(data=request.data)
        if serializator.is_valid():
            User.objects.create_user(**serializator.data)
            return Response({"success": True, "errors": None})
        else:
            return Response(
                {"success": False, "errors": serializator.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_USER,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="put",
    request_body=UpdateUserSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_USER,
    },
)
@swagger_auto_schema(
    method="delete",
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_USER,
    },
)
@api_view(["GET", "PUT", "DELETE"])
@handle_error
def rud_user(request, user_id):
    """Read, update or delete user"""

    if request.method == "GET":
        user = User.objects.get(id=user_id)
        serializator = ReadUserSerializer(user)
        return Response({"data": serializator.data})
    elif request.method == "PUT":
        serializator = UpdateUserSerializer(data=request.data)
        if serializator.is_valid():
            user = User.objects.filter(id=user_id)
            if not user.exists():
                return Response(
                    {
                        "success": False,
                        "errors": "User does not exist.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.update(**serializator.validated_data)
            return Response({"success": True, "errors": None})
    elif request.method == "DELETE":
        user = User.objects.filter(id=user_id)
        if not user.exists():
            return Response(
                {
                    "success": False,
                    "errors": "User does not exist.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.delete()
        return Response({"success": True, "errors": None})


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_ROOM,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="post",
    request_body=CreateRoomSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_DEFAULT,
    },
)
@api_view(["GET", "POST"])
@handle_error
def get_rooms_or_create(request):
    """Read rooms or create new"""

    if request.method == "GET":
        rooms = Room.objects.all()
        serializator = ReadRoomSerializer(rooms, many=True)
        return Response({"data": serializator.data})
    elif request.method == "POST":
        serializator = CreateRoomSerializer(data=request.data)
        if serializator.is_valid():
            Room.objects.create(**serializator.data)
            return Response({"success": True, "errors": None})
        else:
            return Response(
                {"success": False, "errors": serializator.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_ROOM,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="put",
    request_body=UpdateRoomSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_ROOM,
    },
)
@swagger_auto_schema(
    method="delete",
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_ROOM,
    },
)
@api_view(["GET", "PUT", "DELETE"])
@handle_error
def rud_room(request, room_id):
    """Read, update or delete room"""

    if request.method == "GET":
        room = Room.objects.get(id=room_id)
        serializator = ReadRoomSerializer(room)
        return Response({"data": serializator.data})
    elif request.method == "PUT":
        serializator = UpdateRoomSerializer(data=request.data)
        if serializator.is_valid():
            room = Room.objects.filter(id=room_id)
            if not room.exists():
                return Response(
                    {
                        "success": True,
                        "errors": "Room does not exist.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            room.update(**serializator.validated_data)
            return Response({"success": True, "errors": None})
    elif request.method == "DELETE":
        room = Room.objects.filter(id=room_id)
        if not room.exists():
            return Response(
                {
                    "success": True,
                    "errors": "Room does not exist.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        room.delete()
        return Response({"success": True, "errors": None})


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_SUBJECT,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="post",
    request_body=CreateSubjectSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_DEFAULT,
    },
)
@api_view(["GET", "POST"])
@handle_error
def get_subjects_or_create(request):
    """Read subjects or create new"""

    if request.method == "GET":
        subjects = Subject.objects.all()
        serializator = ReadSubjectSerializer(subjects, many=True)
        return Response({"data": serializator.data})
    elif request.method == "POST":
        serializator = CreateSubjectSerializer(data=request.data)
        if serializator.is_valid():
            Subject.objects.create(**serializator.data)
            return Response({"success": True, "errors": None})
        else:
            return Response(
                {"success": False, "errors": serializator.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


@swagger_auto_schema(
    method="get",
    responses={
        200: OK_200_RESPONSE_SUBJECT,
        403: ERROR_403_RESPONSE_DEFAULT,
    },
)
@swagger_auto_schema(
    method="put",
    request_body=UpdateSubjectSerializer,
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_SUBJECT,
    },
)
@swagger_auto_schema(
    method="delete",
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        403: ERROR_403_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_SUBJECT,
    },
)
@api_view(["GET", "PUT", "DELETE"])
@handle_error
def rud_subject(request, subject_id):
    """Read, update or delete subject"""

    if request.method == "GET":
        subject = Subject.objects.get(id=subject_id)
        serializator = ReadSubjectSerializer(subject)
        return Response({"data": serializator.data})
    elif request.method == "PUT":
        serializator = UpdateSubjectSerializer(data=request.data)
        if serializator.is_valid():
            subject = Subject.objects.filter(id=subject_id)
            if not subject.exists():
                return Response(
                    {
                        "success": True,
                        "errors": "Subject does not exist.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            subject.update(**serializator.validated_data)
            return Response({"success": True, "errors": None})
    elif request.method == "DELETE":
        subject = Subject.objects.filter(id=subject_id)
        if not subject.exists():
            return Response(
                {
                    "success": True,
                    "errors": "Subject does not exist.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        subject.delete()
        return Response({"success": True, "errors": None})


@swagger_auto_schema(
    method="post",
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_STUDENT_SUBJECT,
    },
)
@swagger_auto_schema(
    method="delete",
    responses={
        200: OK_200_RESPONSE_DEFAULT,
        404: ERROR_404_RESPONSE_STUDENT_SUBJECT,
    },
)
@api_view(["POST", "DELETE"])
def register_subject(request, user_id, subject_id):
    """Register subject to user"""

    if request.method == "POST":
        user = User.objects.filter(id=user_id)
        if not user.exists():
            return Response(
                {
                    "success": False,
                    "errors": "User doesn't exist.",
                }
            )

        if user[0].permission_id != "5":
            return Response(
                {
                    "success": False,
                    "errors": "User can't register subject.",
                }
            )

        subject = Subject.objects.filter(id=subject_id)
        if not subject.exists():
            return Response(
                {
                    "success": False,
                    "errors": "Subject doesn't exist.",
                }
            )

        StudentSubject.objects.create(
            student=user[0],
            subject=subject[0],
        )
        return Response(
            {
                "success": True,
                "errors": None,
            }
        )
    elif request.method == "DELETE":
        student_subject = StudentSubject.objects.filter(
            student_id=user_id,
            subject_id=subject_id,
        )

        if not student_subject.exists():
            return Response(
                {
                    "success": False,
                    "errors": "Student didn't register subject.",
                }
            )

        student_subject.delete()
        return Response(
            {
                "success": True,
                "errors": None,
            }
        )

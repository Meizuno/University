from drf_yasg import openapi
from education.api.serializators import (
    PermissionSerializer,
    ReadUserSerializer,
    ReadRoomSerializer,
    ReadSubjectSerializer,
)


OK_200_RESPONSE_DEFAULT = openapi.Response(
    "Successful Response",
    examples={
        "application/json": {
            "success": True,
            "errors": None,
        },
    },
)

OK_200_RESPONSE_PERMISSION = openapi.Response(
    "Successful Response",
    schema=PermissionSerializer(many=True),
)

OK_200_RESPONSE_USER = openapi.Response(
    "Successful Response",
    schema=ReadUserSerializer(many=True),
)

OK_200_RESPONSE_SUBJECT = openapi.Response(
    "Successful Response",
    schema=ReadSubjectSerializer(many=True),
)

OK_200_RESPONSE_ROOM = openapi.Response(
    "Successful Response",
    schema=ReadRoomSerializer(many=True),
)


ERROR_403_RESPONSE_DEFAULT = openapi.Response(
    "Permission denied",
    examples={
        "application/json": {
            "success": False,
            "errors": "Permission denied.",
        },
    },
)


ERROR_404_RESPONSE_DEFAULT = openapi.Response(
    "Bad request",
    examples={
        "application/json": {
            "success": False,
            "errors": {
                "additionalProp1": [
                    "string",
                ],
                "additionalProp2": [
                    "string",
                ],
                "additionalProp3": [
                    "string",
                ],
            },
        },
    },
)

ERROR_404_RESPONSE_USER = openapi.Response(
    "Bad request",
    examples={
        "application/json": {
            "success": False,
            "errors": "User does not exist.",
        },
    },
)

ERROR_404_RESPONSE_ROOM = openapi.Response(
    "Bad request",
    examples={
        "application/json": {
            "success": False,
            "errors": "Room does not exist.",
        },
    },
)

ERROR_404_RESPONSE_SUBJECT = openapi.Response(
    "Bad request",
    examples={
        "application/json": {
            "success": False,
            "errors": "Subject does not exist.",
        },
    },
)

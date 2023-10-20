from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.response import Response
from rest_framework import status


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {
                    "success": False,
                    "errors": "Permissions denied.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return func(request, *args, **kwargs)

    return wrapper


def handle_error(func):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as ex:
            raise APIException(detail="An error occurred: " + str(ex))

    return wrapper

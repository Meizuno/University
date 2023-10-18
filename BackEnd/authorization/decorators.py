from rest_framework.exceptions import PermissionDenied, APIException


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Permissions denied.")
        return func(request, *args, **kwargs)
    return wrapper


def handle_error(func):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except Exception as ex:
            raise APIException(detail="An error occurred: " + str(ex))
    return wrapper
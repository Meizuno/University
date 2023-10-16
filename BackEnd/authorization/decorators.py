from rest_framework.exceptions import PermissionDenied


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Permissions denied.")
        return func(request, *args, **kwargs)
    return wrapper
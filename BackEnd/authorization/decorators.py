from rest_framework.exceptions import PermissionDenied


def login_required(func):
    def wrapper(request, *args, **kwargs):
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            raise PermissionDenied("blabla")
        return func(request, *args, **kwargs)
    return wrapper
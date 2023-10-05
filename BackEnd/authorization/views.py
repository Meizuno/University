from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getchoto(request):
    if isinstance(request.user, User):
        choto = [
            "Пользователь авторизирован"
        ]
    else:
        choto = [
            "Пользователь не авторизирован"
        ]
    return Response(choto)
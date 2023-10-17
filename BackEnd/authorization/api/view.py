from rest_framework.response import Response
from rest_framework.decorators import api_view
from authorization.api.serializators import (
    PermissionSerializer, 
    UserSerializator
)
from authorization.models import Permission
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


@swagger_auto_schema(
    method='get',
    query_serializer=PermissionSerializer,
)
@api_view(['GET'])
def get_permissions(request):
    """Get all permission levels"""

    permissions = Permission.objects.all()
    serializator = PermissionSerializer(permissions, many=True)
    return Response({"data": serializator.data})


@swagger_auto_schema(
    method='post',
    request_body=UserSerializator,
)
@api_view(['POST'])
def create_user(request):
    """Create new user"""

    serializator = UserSerializator(data=request.data)
    if serializator.is_valid():
        serializator.save()
        return Response({"data": serializator.data})
    else:
        return Response({"errors": serializator.errors},
                        status=status.HTTP_400_BAD_REQUEST)
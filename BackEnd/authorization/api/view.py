from rest_framework.response import Response
from rest_framework.decorators import api_view
from authorization.api.services import read_permissions
from authorization.api.serializators import PermissionSerializer


@api_view(['GET'])
def get_permissions(request):
    """Get all permission levels"""

    permissions = read_permissions()
    serializator = PermissionSerializer(permissions, many=True)
    return Response(serializator.data)
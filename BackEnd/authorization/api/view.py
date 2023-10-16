from rest_framework.response import Response
from rest_framework.decorators import api_view
from authorization.api.serializators import PermissionSerializer
from authorization.models import Permission


@api_view(['GET'])
def get_permissions(request):
    """Get all permission levels"""

    permissions = Permission.objects.all()
    serializator = PermissionSerializer(permissions, many=True)
    return Response(serializator.data)

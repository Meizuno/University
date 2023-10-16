from authorization.models import Permission


def read_permissions():
    """Reading from db Permission levels"""

    return Permission.objects.all()
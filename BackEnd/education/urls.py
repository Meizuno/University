from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from education.api.view import (
    get_permissions,
    get_users_or_create,
    rud_user,
)


urlpatterns = [
    # User's endpoints
    path('permissions', get_permissions),
    path('user', get_users_or_create),
    path('user/<int:user_id>', rud_user),
]
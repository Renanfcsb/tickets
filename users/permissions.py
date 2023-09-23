from rest_framework.views import Request, View
from rest_framework import permissions
from users.models import User


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:
        return user == request.user or request.user.is_superuser

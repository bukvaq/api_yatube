from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Проверяет наличие прав на изменение/удаление объекта"""

    def has_object_permission(self, request, view, obj):
        return (request.method == 'GET') or (obj.author == request.user)

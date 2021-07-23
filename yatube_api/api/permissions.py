from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Проверяет наличие прав на изменение/удаление объекта"""

    def has_object_permission(self, request, view, obj):
        if request.method in ('PATCH', 'PUT', 'DELETE'):
            return obj.author == request.user
        return True

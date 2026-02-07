from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow read-only access to any authenticated user.
    Write access only to the profile owner.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

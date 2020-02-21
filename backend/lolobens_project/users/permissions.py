from rest_framework import permissions


class IsLoggedInUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # requesting user must be .
        if request.user == obj:
            return True
        else:
            return False


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if bool(request.user.is_superuser and request.user.is_staff):
            return True

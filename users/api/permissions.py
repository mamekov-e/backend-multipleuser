from rest_framework.permissions import BasePermission


class IsEmployeeUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_employee)


class IsDirectorUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_director)

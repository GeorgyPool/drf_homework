from rest_framework.permissions import BasePermission


class IsModer(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.pk

class IsOwnerSubscribe(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class BasicGroupPermission(BasePermission):

    def has_permission(self, request, view):
        group = Group.objects.get(name='basic')
        if request.user.groups.filter(name=group):
            return True
        return False


class ModeratorGroupPermission(BasePermission):

    def has_permission(self, request, view):
        group = Group.objects.get(name='moderator')
        if request.user.groups.filter(name=group):
            return True
        return False

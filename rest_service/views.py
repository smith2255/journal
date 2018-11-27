from rest_framework import viewsets
from notes.models import Note, User
from . import serializers
from .permissions import BasicGroupPermission, ModeratorGroupPermission


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = (
        BasicGroupPermission | ModeratorGroupPermission,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ModeratorGroupPermission,)

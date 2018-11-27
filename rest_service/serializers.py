from rest_framework import serializers
from notes.models import Note, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]
        read_only_fields = ('username',)


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'details',
            'owner'
        ]
        read_only_fields = ('owner',)

from django.test import TestCase
from model_mommy import mommy
from rest_framework import status
from django.contrib.auth.models import Group


class CustomViewSetTest(TestCase):

    def create_user(self, group_name=None):
        user = mommy.make('notes.User')
        if group_name:
            user.groups.add(Group.objects.get(name=group_name))
        return user

    def create_note(self, owner=None):
        if owner:
            return mommy.make('notes.Note', owner=owner)
        return mommy.make('notes.Note')


class NoteViewSetTest(CustomViewSetTest):

    def test_group_permissions(self):
        for group in ('user_group', 'moderator_group'):
            user = self.create_user(group)
            self.client.force_login(user)

            response = self.client.get('/api/notes/')

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

    def test_unauthorized_user(self):
        user = self.create_user()
        self.client.force_login(user)

        response = self.client.get('/api/notes/')

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_unauthenticated_user(self):
        response = self.client.get('/api/notes/')

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_perform_create_sets_user_from_request(self):
        user = self.create_user('user_group')
        note = self.create_note()

        self.client.force_login(user)
        response = self.client.post(
            '/api/notes/',
            data={
                'title': note.title,
                'details': note.details
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data['owner'],
            user.pk
        )

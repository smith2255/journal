from django.test import TestCase
from model_mommy import mommy
from notes.models import Note
from rest_framework import exceptions, status
from django.contrib.auth.models import Group, Permission


class CustomViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        general_group = Group.objects.create(name='moderator')
        general_group = Group.objects.create(name='basic')
        general_perms = Permission.objects.filter(
            codename__in=(
                'add_note',
                'delete_note',
                'change_note',
                'view_note'
            )
        )
        general_group.permissions.add(*general_perms)

    def setUp(self):
        self.general_user = mommy.make('notes.User')
        self.general_user.groups.add(
            Group.objects.get(name='basic')
        )


class NoteViewSetTest(CustomViewSetTest):

    def setUp(self):
        super().setUp()
        self.note = {
            'owner': self.general_user.pk,
            'title': 'DRF Test Title',
            'details': 'These are the details of the note'
        }

    def test_perform_create_with_authorized_user(self):
        self.client.force_login(self.general_user)
        response = self.client.post(
            path='/api/notes/',
            data=self.note
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Note.objects.get(pk=response.data['id']))

    def test_perform_create_with_anonymous_user(self):
        response = self.client.post(
            path='/api/notes/',
            data={
                'title': 'DRF Test Title',
                'details': 'These are the details of the note'
            })

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertIsInstance(
            response.data['detail'],
            exceptions.ErrorDetail
        )

    def test_perform_create_when_user_is_not_authorized(self):
        self.client.force_login(mommy.make('notes.User'))
        response = self.client.post(
            path='/api/notes/',
            data=self.note
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertIsInstance(
            response.data['detail'],
            exceptions.ErrorDetail
        )

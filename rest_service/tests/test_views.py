from django.test import TestCase
from model_mommy import mommy
from notes.models import Note
from rest_framework import exceptions, status


class NoteViewSetTest(TestCase):

    def setUp(self):
        self.user = mommy.make('notes.User')
        self.note = {
            'owner': self.user.pk,
            'title': 'DRF Test Title',
            'details': 'These are the details of the note'}

    def test_perform_create_with_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.post(
            path='/api/notes/',
            data=self.note)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)

        self.assertTrue(Note.objects.get(pk=response.data['id']))

    def test_perform_create_without_authenticated_user(self):
        response = self.client.post(
            path='/api/notes/',
            data={
                'title': 'DRF Test Title',
                'details': 'These are the details of the note'
            })

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN)

        self.assertIsInstance(
            response.data['detail'],
            exceptions.ErrorDetail)

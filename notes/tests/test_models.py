import uuid

from django.test import TestCase
from model_mommy import mommy


class UserModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make('notes.User')

    def test_pk_is_of_type_uuid(self):
        self.assertIsInstance(self.user.pk, uuid.UUID)


class NoteModelTest(TestCase):

    def setUp(self):
        self.note = mommy.make('notes.Note')

    def test_create(self):
        self.assertEqual(
            str(self.note),
            self.note.title
        )

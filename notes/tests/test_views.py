import ipdb

from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy


class NoteDetailViewTest(TestCase):

    def setUp(self):
        self.note = mommy.make('notes.Note')

    def test_get_note_details(self):
        path = reverse('notes:note-detail', kwargs={'pk': self.note.pk})
        response = self.client.get(path=path)
        content = str(response.content)
        self.assertTrue(content.find(self.note.title))
        self.assertTrue(content.find(self.note.details))
        self.assertEqual(response.status_code, 200)


class NoteListViewTest(TestCase):

    def setUp(self):
        self.notes = mommy.make('notes.Note', 5)

    def test_get_note_list(self):
        path = reverse('notes:note-list')
        response = self.client.get(path=path)
        content = str(response.content)
        self.assertTrue(content.find(self.notes[0].title))
        self.assertTrue(content.find(self.notes[3].details))
        self.assertEqual(response.status_code, 200)

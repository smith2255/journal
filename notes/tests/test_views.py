from django.test import tag, TestCase
from django.urls import reverse
from model_mommy import mommy


class NoteDetailViewTest(TestCase):

    def setUp(self):
        self.note = mommy.make('notes.Note')

    @tag('smoke')
    def test_get_note_details(self):
        path = reverse('notes:note-detail', kwargs={'pk': self.note.pk})
        response = self.client.get(path=path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['note'], self.note)


class NoteListViewTest(TestCase):

    def setUp(self):
        self.notes = mommy.make('notes.Note', 5)

    @tag('smoke')
    def test_get_note_list(self):
        path = reverse('notes:note-list')
        response = self.client.get(path=path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['note_list']), 5)


class NoteCreateViewTest(TestCase):

    @tag('smoke')
    def test_create_note(self):
        user = mommy.make('notes.User')
        title = 'My Random Note'
        details = 'This is a simple note'
        self.client.force_login(user)

        response = self.client.post(
            reverse('notes:note-create'),
            {'title': title, 'details': details},
            follow=True
        )
        posted_note = response.context_data.get('note')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(posted_note.details, details)
        self.assertEqual(posted_note.title, title)


class NoteUpdateViewTest(TestCase):

    @tag('smoke')
    def test_update_note(self):
        note = mommy.make('notes.Note')
        title = 'title change'
        details = 'detail change'
        response = self.client.post(
            reverse('notes:note-update', kwargs={'pk': note.pk}),
            {'title': title, 'details': details},
            follow=True
        )
        note.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['note'], note)


class NoteDeleteViewTest(TestCase):

    @tag('smoke')
    def test_update_note(self):
        note = mommy.make('notes.Note')
        response = self.client.delete(
            reverse('notes:note-delete', kwargs={'pk': note.pk}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context['note'], note)

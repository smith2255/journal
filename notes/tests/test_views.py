from django.test import tag, TestCase
from django.urls import reverse
from model_mommy import mommy
from ..models import Note
from django.contrib.auth.models import Permission, Group


class CustomViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        general_group = Group.objects.create(name='General')
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
            Group.objects.get(name='General')
        )


class NoteDetailViewTest(CustomViewTest):

    @tag('smoke')
    def test_get_note_detail(self):
        note = mommy.make('notes.Note')

        self.client.force_login(self.general_user)
        response = self.client.get(
            reverse(
                'notes:note-detail',
                kwargs={'pk': note.pk}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['note'], note)

    @tag('smoke')
    def test_does_not_have_view_note_permission(self):
        note = mommy.make('notes.Note')

        self.client.force_login(mommy.make('notes.User'))
        response = self.client.get(
            reverse(
                'notes:note-detail',
                kwargs={'pk': note.pk}
            ))

        self.assertEqual(response.status_code, 403)


class NoteListViewTest(CustomViewTest):

    @tag('smoke')
    def test_get_note_list(self):
        mommy.make('notes.Note', 5)

        self.client.force_login(self.general_user)
        response = self.client.get(reverse('notes:note-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['note_list']), 5)

    @tag('smoke')
    def test_does_not_have_list_note_permission(self):
        self.client.force_login(mommy.make('notes.User'))

        response = self.client.get(reverse('notes:note-list'))

        self.assertEqual(response.status_code, 403)


class NoteCreateViewTest(CustomViewTest):

    @tag('smoke')
    def test_create_note(self):
        title = 'My Random Note'
        details = 'This is a simple note'

        self.client.force_login(self.general_user)
        response = self.client.post(
            reverse('notes:note-create'),
            {'title': title, 'details': details},
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        posted_note = response.context_data.get('note')

        self.assertEqual(posted_note.details, details)
        self.assertEqual(posted_note.title, title)

    @tag('smoke')
    def test_does_not_have_add_note_permission(self):
        self.client.force_login(mommy.make('notes.User'))

        response = self.client.get(reverse('notes:note-create'))

        self.assertEqual(response.status_code, 403)


class NoteUpdateViewTest(CustomViewTest):

    @tag('smoke')
    def test_update_note(self):
        note = mommy.make('notes.Note')
        title = 'title change'
        details = 'detail change'

        self.client.force_login(self.general_user)
        response = self.client.post(
            reverse(
                'notes:note-update',
                kwargs={'pk': note.pk}
            ),
            {'title': title, 'details': details},
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['note'], note)

    @tag('smoke')
    def test_does_not_have_change_note_permission(self):
        note = mommy.make('notes.Note')

        self.client.force_login(mommy.make('notes.User'))
        response = self.client.post(
            reverse(
                'notes:note-update',
                kwargs={'pk': note.pk}
            ),
            follow=True
        )

        self.assertEqual(response.status_code, 403)


class NoteDeleteViewTest(CustomViewTest):

    @tag('smoke')
    def test_update_note(self):
        note = mommy.make('notes.Note')

        self.client.force_login(self.general_user)
        response = self.client.delete(
            reverse(
                'notes:note-delete',
                kwargs={'pk': note.pk}
            ),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(pk=note.pk)

    @tag('smoke')
    def test_does_not_have_delete_note_permission(self):
        note = mommy.make('notes.Note')

        self.client.force_login(mommy.make('notes.User'))
        response = self.client.post(
            reverse(
                'notes:note-delete',
                kwargs={'pk': note.pk}
            ),
            follow=True
        )

        self.assertEqual(response.status_code, 403)

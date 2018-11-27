from rest_framework import status
from .test_base import JournalBaseTest


class NoteViewSetTest(JournalBaseTest):

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

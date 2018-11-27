from collections import OrderedDict
from .test_base import JournalBaseTest
from ..serializers import UserSerializer, NoteSerializer


class UserSerializerTest(JournalBaseTest):

    def test_basic_serialize(self):
        user = self.create_user()
        expected = {
            'id': str(user.pk),
            'username': user.username,
        }

        user_serializer = UserSerializer(user)
        actual = user_serializer.data
        self.assertEqual(actual, expected)

    def test_basic_deserialize(self):
        expected_data = OrderedDict((
            ('username', 'random'),
        ))
        test_data = expected_data.copy()
        test_data['id'] = 'fdsaf'

        user_serializer = UserSerializer(data=test_data)

        self.assertTrue(user_serializer.is_valid())
        self.assertEqual(
            user_serializer.data,
            expected_data
        )


class NoteSerializerTest(JournalBaseTest):

    def test_basic_serialize(self):
        user = self.create_user()
        note = self.create_note(user)
        expected = {
            'id': str(note.pk),
            'title': note.title,
            'details': note.details,
            'owner': user.pk
        }

        note_serializer = NoteSerializer(note)
        actual = note_serializer.data
        self.assertEqual(actual, expected)

    def test_basic_deserialize(self):
        expected_data = OrderedDict((
            ('title', 'title_01'),
            ('details', 'details_01')
        ))
        test_data = expected_data.copy()
        test_data['id'] = 'fdsaf'
        test_data['owner'] = 'lafdsaf'

        note_serializer = NoteSerializer(data=test_data)

        self.assertTrue(note_serializer.is_valid())
        self.assertEqual(
            note_serializer.data,
            expected_data
        )

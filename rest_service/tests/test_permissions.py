from unittest import mock
from .test_base import JournalBaseTest
from ..permissions import ModeratorGroupPermission, UserGroupPermission


class UserGroupPermissionTest(JournalBaseTest):

    def test_user_has_permission(self):
        user = self.create_user('user_group')
        mock_request = mock.MagicMock(user=user)

        result = UserGroupPermission().has_permission(
            mock_request,
            mock.MagicMock()
        )

        self.assertTrue(result)

    def test_user_does_not_have_permission(self):
        user = self.create_user()
        mock_request = mock.MagicMock(user=user)

        result = UserGroupPermission().has_permission(
            mock_request,
            mock.MagicMock()
        )

        self.assertFalse(result)


class ModeratorGroupPermissionTest(JournalBaseTest):

    def test_user_has_permission(self):
        user = self.create_user('moderator_group')
        mock_request = mock.MagicMock(user=user)

        result = ModeratorGroupPermission().has_permission(
            mock_request,
            mock.MagicMock()
        )

        self.assertTrue(result)

    def test_user_does_not_have_permission(self):
        user = self.create_user()
        mock_request = mock.MagicMock(user=user)

        result = ModeratorGroupPermission().has_permission(
            mock_request,
            mock.MagicMock()
        )

        self.assertFalse(result)

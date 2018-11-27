from django.contrib.auth.models import Group
from django.test import TestCase
from model_mommy import mommy


class JournalBaseTest(TestCase):

    def create_user(self, group_name=None):
        user = mommy.make('notes.User')
        if group_name:
            user.groups.add(Group.objects.get(name=group_name))
        return user

    def create_note(self, owner=None):
        if owner:
            return mommy.make('notes.Note', owner=owner)
        return mommy.make('notes.Note')

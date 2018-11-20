from django.views import generic
from .models import Note


class NoteDetailView(generic.DetailView):

    model = Note


class NoteListView(generic.ListView):

    model = Note

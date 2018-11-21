from django.views import generic
from .models import Note


class NoteDetailView(generic.DetailView):

    model = Note


class NoteListView(generic.ListView):

    model = Note
    # TODO: Sort by: Last Edited
    # e.g. queryset = Note.objects.order_by('-last_edited')


class NoteCreateView(generic.CreateView):

    model = Note
    fields = ['title', 'details']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        kwargs['owner'] = self.request.user
        return super().get_context_data(*args, **kwargs)

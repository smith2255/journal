from django.urls import reverse_lazy
from django.views import generic
from .models import Note


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('notes:note-list')


class NoteDetailView(generic.DetailView):
    model = Note


class NoteListView(generic.ListView):
    model = Note
    # TODO: add this in:
    # queryset = Note.objects.order_by('-last_edited')


class NoteCreateView(generic.CreateView):

    model = Note
    fields = ['title', 'details']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        kwargs['owner'] = self.request.user
        return super().get_context_data(*args, **kwargs)


class NoteUpdateView(generic.UpdateView):

    model = Note
    fields = ['title', 'details']

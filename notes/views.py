from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Note


class NoteDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'notes.delete_note'
    model = Note
    success_url = reverse_lazy('notes:note-list')


class NoteDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'notes.view_note'
    model = Note
    login_url = '/admin/login/'


class NoteListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'notes.view_note'
    model = Note
    queryset = Note.objects.order_by('-last_edited')


class NoteCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'notes.add_note'
    model = Note
    fields = ['title', 'details']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoteUpdateView(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'notes.change_note'
    model = Note
    fields = ['title', 'details']

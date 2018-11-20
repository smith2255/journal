from django.urls import path
from .views import NoteDetailView, NoteListView

app_name = 'notes'

urlpatterns = [
    path(
        'note/',
        NoteListView.as_view(),
        name='note-list'
    ),
    path(
        'note/<uuid:pk>/',
        NoteDetailView.as_view(),
        name='note-detail'
    )
]

from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path(
        '',
        views.NoteListView.as_view(),
        name='note-list'
    ),

    path(
        'create/',
        views.NoteCreateView.as_view(),
        name='note-create'
    ),
    path(
        '<uuid:pk>/',
        views.NoteDetailView.as_view(),
        name='note-detail'
    ),
    path(
        '<uuid:pk>/update/',
        views.NoteUpdateView.as_view(),
        name='note-update'
    ),
    path(
        '<uuid:pk>/remove/',
        views.NoteDeleteView.as_view(),
        name='note-delete'
    )
]

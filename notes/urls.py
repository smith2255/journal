from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path(
        'notes/',
        views.NoteListView.as_view(),
        name='note-list'
    ),
    path(
        'notes/create/',
        views.NoteCreateView.as_view(),
        name='note-create'
    ),
    path(
        'notes/<uuid:pk>/',
        views.NoteDetailView.as_view(),
        name='note-detail'
    ),
    path(
        'notes/<uuid:pk>/add/',
        views.NoteUpdateView.as_view(),
        name='note-update'
    ),
    path(
        'notes/<uuid:pk>/remove/',
        views.NoteDeleteView.as_view(),
        name='note-delete'
    )
]

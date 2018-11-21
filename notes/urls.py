from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path(
        'note/',
        views.NoteListView.as_view(),
        name='note-list'
    ),
    path(
        'note/create/',
        views.NoteCreateView.as_view(),
        name='note-create'
    ),
    path(
        'note/<uuid:pk>/',
        views.NoteDetailView.as_view(),
        name='note-detail'
    )
]

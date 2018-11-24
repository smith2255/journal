# import ipdb
# import pprint
from . import views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('notes', views.NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='notesapi'
        )
    )
]

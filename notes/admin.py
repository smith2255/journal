from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Note, User


admin.site.register(Note)
admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import *

class NoteAdminView(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email','password']

# Register your models here.

admin.site.register(User, NoteAdminView)
from django.contrib import admin
from .models import *

class NoteAdminView(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','date']

# Register your models here.

admin.site.register(Note, NoteAdminView)
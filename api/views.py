from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.models import Note
from api.serializer import NoteSerializer


# Create your views here.

class noteView(ReadOnlyModelViewSet):
    dic = {
        "request": 200,
        "model": Note.objects.all()
    }
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

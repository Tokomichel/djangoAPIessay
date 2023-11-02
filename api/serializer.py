from rest_framework import serializers
from api.models import *

class NoteSerializer(serializers.Serializer):

    titre = serializers.CharField(max_length=20, source='title')
    Contenu = serializers.CharField(max_length=40, source='content')
    Cree = serializers.DateField(source='date')

    class Meta:
        model = Note
        fields = "__all__"
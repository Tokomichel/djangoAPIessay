from datetime import datetime

from rest_framework import serializers
from api.models import *

class NoteSerializer(serializers.Serializer):

    # toko = serializers.SerializerMethodField(method_name="to_upper")
    titre = serializers.CharField(max_length=20, source='title')
    Contenu = serializers.CharField(max_length=40, source='content')
    Cree = serializers.DateField(source='date')

    def to_upper(self, obj):
        return obj.title.upper()

    def create(self, validated_data):
        print(validated_data)
        note = Note()
        note.title = validated_data["title"]
        note.content = validated_data["content"]
        note.date = validated_data["date"]
        note.save()

        return note
    class Meta:
        model = Note
        exclude = ['titre']
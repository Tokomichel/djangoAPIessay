from datetime import datetime

from rest_framework import serializers
from api.models import *

class NoteSerializer(serializers.Serializer):

    toko = serializers.SerializerMethodField(method_name="to_upper")
    Contenu = serializers.CharField(max_length=40, source='content')
    Cree = serializers.DateField(source='date')

    def to_upper(self, obj):
        return obj.title.upper()
    class Meta:
        model = Note
        exclude = ['titre']
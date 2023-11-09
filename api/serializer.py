from datetime import datetime

from rest_framework import serializers
from api.models import *
from  log.models import *

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

class UserApi(serializers.Serializer):
    user_name = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)

    def create(self, validated_data):
        user = User()
        user.user_name = validated_data['user_name']
        user.email = validated_data['email']
        user.password = validated_data['password']

        user.save()
        return user

    class Meta:
        model = User

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from rest_framework import viewsets, status, request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.models import Note
from api.serializer import NoteSerializer


# Create your views here.

class noteView(ModelViewSet):
    dic = {
        "request": 200,
        "model": Note.objects.all()
    }
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ApiViewSet(APIView):

    def get(self, req: request.Request):
        obj = Note.objects.all()
        serializer = NoteSerializer(data=obj, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    def post(self, req):
        serializer = NoteSerializer(data=req.data)
        print(f"{serializer.is_valid()}  {req.data}")
        if serializer.is_valid():
            # print(f"{serializer.data}")
            # print(f"{serializer.is_valid()}")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def create(self):
        print()
        # {
        #     "id": "4",
        #     "title": "eo0rpm",
        #     "content": "iowekdc",
        #     "date": "2021-12-02"
        # }
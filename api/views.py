from rest_framework import viewsets, status, request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Note
from  log.models import User
from api.serializer import NoteSerializer, UserApi


# Create your views here.

class noteView(ModelViewSet):
    dic = {
        "request": 200,
        "model": Note.objects.all()
    }
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserApi

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

        msg = {"msg": "tu as fais une mauvaise requete", "data_recue": f"{req.data}"}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def update(self, req):
        serializer = NoteSerializer(data=req.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteDetailView(APIView):
    def get(self, request: request.Request, id: int):
        try:
            obj = Note.objects.get(id=id)
        except Note.DoesNotExist:
            msg = {"msg": f"l'element d'id: {id} n'existe pas dans la base de donnees"}

            return Response(data=msg, status=status.HTTP_404_NOT_FOUND)


        serializer = NoteSerializer(data=obj, many=False)
        print(f"{serializer.is_valid()} {Note.objects.all()[0].id} {id} {obj.id} {Note.objects.get(id=id).id} {request.data} {request.POST}")
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        print(f"{serializer.data}")
        di = {
            "id": f"{obj.id}",
            "title": f"{obj.title}",
            "content": f"{obj.content}",
            "date": f"{obj.date}"
        }
        return Response(data=di, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: request.Request, id: int):
        try:
            obj = Note.objects.get(id=id)
        except Note.DoesNotExist:
            msg = {"msg": f"l'element d'id: {id} n'existe pas dans la base de donnees"}

        serializer = NoteSerializer(instance=obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
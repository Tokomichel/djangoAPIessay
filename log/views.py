from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
# from api.models import *
from log.models import User


# Create your views here.

def maVue(req: WSGIRequest):
    message = ""
    if req.method == 'POST':
        use = User.objects.all()
        result: object

        for el in use:
             if el.user_name == req.POST["login"]:
                result = el
                if el.password == req.POST["pwd"]:
                     print("okay")
                else:
                    message = "Erreur de nom du mot de passe"
                    return HttpResponse("<H1><center>Erreur du mot de passe ou du nom d'utilisateur</center></H1>")
             else:
               return HttpResponse("<H1><center>Erreur du mot de passe ou du nom d'utilisateur</center></H1>")

        return HttpResponse("<H1> <center> Connexion Reussie </center></H1>")


    return render(req, "index.html", {})

def createUser(req: WSGIRequest):
    message = ""
    if req.method == 'POST':
        user = User()
        user.user_name = req.POST["user_name"]
        user.email = req.POST['email']
        user.password = req.POST['password']
        user.save()

        return HttpResponse("<H1> <center> Creation Reussie </center></H1>")
    return render(req, 'user.html', {})
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def toko_views(req: WSGIRequest):

    if req.method == 'POST':
        print(req.POST["pwd"])
    return render(req, "index.html", {})
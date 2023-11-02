from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def maVue(request):
    return HttpResponse("<H1> Okay </H1>")
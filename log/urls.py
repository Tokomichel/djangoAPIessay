from django.urls import path
from . import views

urlpatterns = [
    path('', views.maVue),
    path('/user', views.createUser)
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import api.views
from . import views
from api.urls import router as note_router

router = routers.DefaultRouter()
router.registry.extend(note_router.registry)

urlpatterns = [
    path('manage/', admin.site.urls),
    path('toko', views.toko_views),
    path('log', include('log.urls')),
    path('post', api.views.ApiViewSet.as_view()),
    path('crud/<int:id>/', api.views.NoteDetailView.as_view()), # get one
    path('', include(router.urls))
]

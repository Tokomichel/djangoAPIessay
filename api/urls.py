from rest_framework import routers

from api.views import noteView

router = routers.DefaultRouter()

router.register("notes", noteView)
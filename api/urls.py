from rest_framework import routers

from api.views import noteView, ApiViewSet

router = routers.DefaultRouter()

router.register("notes", noteView)
# router.register("post", ApiViewSet.as_view())
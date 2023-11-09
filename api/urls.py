from rest_framework import routers

from api.views import noteView, ApiViewSet, UserView

router = routers.DefaultRouter()

router.register("notes", noteView) # GET POST
router.register('user', UserView) #Get post

# router.register("post", ApiViewSet.as_view())
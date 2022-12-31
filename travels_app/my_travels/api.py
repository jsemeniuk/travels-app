from rest_framework import routers

from my_travels.viewsets import PlacesViewSet

router = routers.DefaultRouter()
router.register(r"my_travels", PlacesViewSet)

urlpatterns = router.urls
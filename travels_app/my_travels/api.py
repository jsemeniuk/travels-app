from rest_framework import routers

from my_travels.viewsets import PlacesViewSet

router = routers.DefaultRouter()
router.register(r"my_travels", PlacesViewSet, basename="main_page")

urlpatterns = router.urls
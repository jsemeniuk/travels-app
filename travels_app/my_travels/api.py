from rest_framework import routers

from my_travels.viewsets import PlacesVisitedViewSet, WishlistViewSet

router = routers.DefaultRouter()
router.register(r"visited_places", PlacesVisitedViewSet, basename="main_page")
router.register(r"wishlist", WishlistViewSet, basename="main_page")

urlpatterns = router.urls
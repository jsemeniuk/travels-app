from django.urls import path

from .views import TravelsMapView

urlpatterns = [
    path("map/", TravelsMapView.as_view()),
]
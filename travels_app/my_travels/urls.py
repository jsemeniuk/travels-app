from django.urls import path

from . import views

urlpatterns = [
    path("map/", views.TravelsMapView.as_view()),
    path('map/<int:pk>/', views.place_detail, name='place_detail'),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.TravelsMapView.as_view(), name='main_page'),
    path('<int:pk>/', views.place_detail, name='place_detail'),
    path('<int:pk>/edit/', views.place_edit, name='place_edit'),
    path('new/location=<location>', views.place_new, name='place_new'),
]
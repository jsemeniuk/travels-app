from django.urls import path

from . import views

urlpatterns = [
    path("", views.TravelsMapView.as_view(), name='main_page'),
    path('places', views.places_all, name='places_all'),
    path('<int:pk>/', views.place_detail, name='place_detail'),
    path('<int:pk>/edit/', views.place_edit, name='place_edit'),
    path('new/location=<location>', views.place_new, name='place_new'),
    path('<int:pk>/list/', views.place_check_list_exists, name='place_check_list_exists'),
    path('<int:pk>/tag/new', views.add_tag, name='add_tag'),
]
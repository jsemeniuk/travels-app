from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", login_required(views.TravelsMapView.as_view(), login_url="login"), name='main_page'),
    path('places', login_required(views.SearchResultsList.as_view(), login_url="login"), name='places_all'),
    path('places/<int:tag_id>', views.SearchResultsList.as_view(), name='places_tag'),
    path('<int:pk>/', views.place_detail, name='place_detail'),
    path('<int:pk>/edit/', views.place_edit, name='place_edit'),
    path('new/location=<location>', views.place_new, name='place_new'),
    path('<int:pk>/list/', views.place_check_list_exists, name='place_check_list_exists'),
    path('<int:pk>/tag/new', views.add_tag, name='add_tag'),
    path('place/delete/<int:pk>', views.delete_place, name='delete_place'),
]
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('trip_plans', login_required(views.SearchResultsList.as_view(), login_url="login"), name='trips_all'),
    path('trip/new', views.trip_plan_new, name='trip_plan_new'),
    path('trip/<int:pk>/', views.trip_details, name='trip_details'),
    path('trip/<int:pk>/edit/', views.trip_plan_edit, name='trip_plan_edit'),
    path('<int:pk>/tag/new', views.add_tag_for_trip, name='add_tag_for_trip'),
    path('trip/delete/<int:pk>', views.delete_trip, name='delete_trip'),
]
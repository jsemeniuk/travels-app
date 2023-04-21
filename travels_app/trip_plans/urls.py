from django.urls import path

from . import views

urlpatterns = [
    path('trip_plans', views.trips_all, name='trips_all'),
    path('trip/new', views.trip_plan_new, name='trip_plan_new'),
    path('trip/<int:pk>/', views.trip_details, name='trip_details'),
    path('trip/<int:pk>/edit/', views.trip_plan_edit, name='trip_plan_edit'),
    
]
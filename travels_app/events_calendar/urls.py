from django.urls import path

from . import views

urlpatterns = [
    path('events', views.events_list, name='events_list'),
    path('events/month=<month>&year=<year>', views.events_list, name='events_list'),
    path('event/new', views.event_new, name='event_new'),
    path('event/<int:pk>/', views.event_details, name='event_details'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/delete/<int:pk>', views.delete_event, name='delete_event'),
]
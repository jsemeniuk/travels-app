from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('events', views.events_calendar, name='events_calendar'),
    path('events/month=<month>year=<year>', views.events_calendar, name='events_calendar'),
    path('event/new', views.event_new, name='event_new'),
    path('event/<int:pk>/', views.event_details, name='event_details'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/delete/<int:pk>', views.delete_event, name='delete_event'),
]
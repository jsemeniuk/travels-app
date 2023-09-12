"""travels_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from django.conf.urls import handler404
from lists.views import lists_all
from my_travels.views import SearchResultsList

handler404 = 'my_travels.views.handler404'
handler400 = 'my_travels.views.handler400'
handler500 = 'my_travels.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("my_travels.api")),
    path("", include("my_travels.urls")), 
    path("", include("lists.urls")), 
    path("", include("trip_plans.urls")), 
    path("", include("events_calendar.urls")), 
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]

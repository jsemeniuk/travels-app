from django.contrib.gis import admin
from django.contrib import admin as ad
from .models import PlacesVisited, UserConfig

admin.site.register(PlacesVisited, admin.GISModelAdmin)
ad.site.register(UserConfig)

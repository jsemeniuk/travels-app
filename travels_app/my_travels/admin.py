from django.contrib.gis import admin
from .models import PlacesVisited

admin.site.register(PlacesVisited, admin.GISModelAdmin)

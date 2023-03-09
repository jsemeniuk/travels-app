from django.contrib.gis import admin
from .models import Places, ChecklistsForPlaces

admin.site.register(Places, admin.GISModelAdmin)
admin.site.register(ChecklistsForPlaces)

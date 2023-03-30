from django.contrib.gis import admin
from .models import Places

admin.site.register(Places, admin.GISModelAdmin)


from django.contrib.gis import admin
from .models import Places, Tag

admin.site.register(Places, admin.GISModelAdmin)
admin.site.register(Tag, admin.GISModelAdmin)


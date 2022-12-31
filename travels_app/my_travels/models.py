from django.contrib.gis.db import models

class PlacesVisited(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    visit_date = models.DateField()
    description = models.CharField(max_length=1000)
    photo = models.FileField(upload_to='travel_photos', blank=True)


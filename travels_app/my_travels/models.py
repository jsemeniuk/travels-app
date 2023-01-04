from django.conf import settings
from django.contrib.gis.db import models

User= settings.AUTH_USER_MODEL

class PlacesVisited(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    visit_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    photo = models.FileField(upload_to='travel_photos', blank=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)


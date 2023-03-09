from django.conf import settings
from django.contrib.gis.db import models
from django.db import models as dbmodels

User= settings.AUTH_USER_MODEL

class Places(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    visit_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    photo = models.FileField(upload_to='travel_photos', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    VISTITED = 'AV'
    WISHLIST = 'WI'
    GROUP_CHOICES = [
        (VISTITED, 'Already Visited'),
        (WISHLIST, 'Wishlist')]
    group = models.CharField(
        max_length=2,
        choices=GROUP_CHOICES,
        default=VISTITED,
    )

class ChecklistsForPlaces(models.Model):
    item = models.CharField(max_length=100)
    item_done = models.BooleanField(default=False)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)


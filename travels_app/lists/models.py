from django.conf import settings
from django.db import models
from my_travels.models import Places

User= settings.AUTH_USER_MODEL

class Lists(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    place_id = models.ForeignKey(Places, on_delete=models.CASCADE, blank=True, null=True)
 
class Items(models.Model):
    name = models.CharField(max_length=100)
    item_done = models.BooleanField(default=False)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)

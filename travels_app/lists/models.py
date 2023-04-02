from django.db import models
from my_travels.models import Places

class Lists(models.Model):
    name = models.CharField(max_length=100)
    place_id = models.ForeignKey(Places, on_delete=models.CASCADE, blank=True, null=True)
 
class Items(models.Model):
    name = models.CharField(max_length=100)
    item_done = models.BooleanField(default=False)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)

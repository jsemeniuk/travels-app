from django.db import models

class Lists(models.Model):
    name = models.CharField(max_length=100)
 
class Items(models.Model):
    name = models.CharField(max_length=100)
    item_done = models.BooleanField(default=False)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)

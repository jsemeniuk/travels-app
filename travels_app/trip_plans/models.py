from django.db import models
from my_travels.models import Places
from lists.models import Lists
from django.conf import settings
from ckeditor.fields import RichTextField
User= settings.AUTH_USER_MODEL

class TripPlan(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    details = RichTextField(blank=True)
    lists = models.ForeignKey(Lists, on_delete=models.CASCADE, blank=True, null=True)
    places = models.ManyToManyField(Places, blank=True, null=True)
    done = models.BooleanField(default=False)

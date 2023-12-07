from django.db import models
from my_travels.models import Places, Tag
from django.conf import settings
from ckeditor.fields import RichTextField
User= settings.AUTH_USER_MODEL

class Event(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    details = RichTextField(blank=True)
    places = models.ManyToManyField(Places, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)

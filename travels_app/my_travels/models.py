from django.conf import settings
from django.contrib.gis.db import models
from django.db import models as dbmodels
from ckeditor.fields import RichTextField

User= settings.AUTH_USER_MODEL

class Tag(dbmodels.Model):
    tag = dbmodels.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.tag

class Places(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    visit_date = models.DateField(blank=True)
    description = RichTextField(blank=True)
    photo = models.FileField(upload_to='travel_photos', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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
    tag = dbmodels.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name





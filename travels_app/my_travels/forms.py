from django import forms
from django.contrib.gis import forms
from .models import PlacesVisited

class PlaceForm(forms.ModelForm):
    location = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    class Meta:
        model = PlacesVisited
        fields = ("name", "visit_date", "description", "location")
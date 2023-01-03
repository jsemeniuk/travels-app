from django import forms
from .models import PlacesVisited

class PlaceForm(forms.ModelForm):

    class Meta:
        model = PlacesVisited
        fields = ("name", "visit_date", "description", "location")
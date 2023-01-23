from django import forms
from django.contrib.gis import forms
from .models import PlacesVisited
from datetime import datetime
from django.contrib.admin import widgets 

class NewPlaceForm(forms.ModelForm):
    visit_date = forms.DateField(
            widget=widgets.AdminDateWidget(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y'],
            initial=datetime.today()
            )
    class Meta:
        model = PlacesVisited
        fields = ("name", "visit_date", "description")

class EditPlaceForm(forms.ModelForm):
    location = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 
                                'map_height': 500}))
    visit_date = forms.DateField(
            widget=widgets.AdminDateWidget(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y'],
            initial=datetime.today()
            )
    class Meta:
        model = PlacesVisited
        fields = ("name", "visit_date", "description", "location")
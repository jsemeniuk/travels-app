from django import forms 
from django.contrib.gis import forms
from .models import Places
from datetime import datetime
from django.contrib.admin import widgets 

class PlaceForm(forms.ModelForm):
    visit_date = forms.DateField(
            label='Date',
            widget=widgets.AdminDateWidget(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y'],
            initial=datetime.today()
            )

class NewPlaceForm(PlaceForm):
    class Meta:
        model = Places
        fields = ("name", "visit_date", "description", "group")

class EditPlaceForm(PlaceForm):
    location = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_height': 500}))
    class Meta:
        model = Places
        fields = ("name", "visit_date", "description", "group", "location")
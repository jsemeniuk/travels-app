from django import forms 
from django.contrib.gis import forms
from .models import Places, Tag
from datetime import datetime
from django.contrib.admin import widgets 

class PlaceForm(forms.ModelForm):
    name =forms.CharField(
        label='Place\'s name',
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    visit_date = forms.DateField(
            label='Visit\'s date',
            widget=widgets.AdminDateWidget(attrs={"class": "form-control", "type": "date", "value": datetime.today() }),
            )

class NewPlaceForm(PlaceForm):
    class Meta:
        model = Places
        fields = ("name", "visit_date")

class EditPlaceForm(PlaceForm):
    location = forms.PointField(widget=forms.TextInput(attrs={'type': "hidden"}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tag"].widget.attrs.update({"class": "form-select"})


    class Meta:
        model = Places
        fields = ("name", "visit_date", "description", "location", "tag")


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("tag", )
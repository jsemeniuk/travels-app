from django import forms 
from .models import Event
from django.contrib.admin import widgets 
from datetime import datetime, timedelta
from my_travels.models import Places

class EventForm(forms.ModelForm):
    name = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={"class": "form-control"})
        )

    start_date = forms.DateField(
            label='From',
            widget=widgets.AdminDateWidget(attrs={"class": "form-control date-field", "type": "date", "value": datetime.today() }),
            )

    #TODO Add validation for end_date to be after start_date
    end_date = forms.DateField(
            label='To',
            widget=widgets.AdminDateWidget(attrs={"class": "form-control date-field", "type": "date", "value": datetime.today() }),
            )


class AddNewEventForm(EventForm):

    class Meta:
        model = Event
        fields = ("name", "start_date", "end_date")


class EditEventForm(EventForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs) 

    class Meta:
        model = Event
        fields = ("name", "start_date", "end_date", "details", "places", "tag")
from django import forms 
from .models import TripPlan
from django.contrib.admin import widgets 
from datetime import datetime, timedelta
from my_travels.models import Places

class TripPlanForm(forms.ModelForm):
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


class AddNewPlanForm(TripPlanForm):

    class Meta:
        model = TripPlan
        fields = ("name", "start_date", "end_date")


class EditPlanForm(TripPlanForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['places'].queryset = Places.objects.filter(user=user).filter(group="WI")

    class Meta:
        model = TripPlan
        fields = ("name", "start_date", "end_date", "details", "places", "tag")
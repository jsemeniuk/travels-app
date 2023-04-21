from django import forms 
from .models import TripPlan
from django.contrib.admin import widgets 
from datetime import datetime, timedelta

class TripPlanForm(forms.ModelForm):
    start_date = forms.DateField(
            label='Start Date',
            widget=widgets.AdminDateWidget(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y'],
            initial=datetime.today() + timedelta(days=1)
            )

    end_date = forms.DateField(
            label='End Date',
            widget=widgets.AdminDateWidget(format='%d.%m.%Y'),
            input_formats=['%d.%m.%Y'],
            initial=datetime.today() + timedelta(days=2)
            )


class AddNewPlanForm(TripPlanForm):

    class Meta:
        model = TripPlan
        fields = ("name", "start_date", "end_date")


class EditPlanForm(TripPlanForm):

    class Meta:
        model = TripPlan
        fields = ("name", "start_date", "end_date", "trip_details", "journey_details")
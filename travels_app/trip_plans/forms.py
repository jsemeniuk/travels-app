from django import forms 
from .models import TripPlan
from django.contrib.admin import widgets 
from datetime import datetime, timedelta
from my_travels.models import Places

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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['places'].queryset = Places.objects.filter(user=user).filter(group="WI")

    class Meta:
        model = TripPlan
        fields = ("name", "start_date", "end_date", "details", "places")
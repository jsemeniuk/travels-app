from django import forms 
from .models import Items, Lists

class ManageItems(forms.ModelForm):
    item_done = forms.BooleanField(required=False)
    class Meta:
        model = Items
        fields = ("item_done", "name",)

class ManageLists(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ("name",)
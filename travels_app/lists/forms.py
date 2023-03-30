from django import forms 
from .models import Items, Lists

class ManageItems(forms.ModelForm):
    class Meta:
        model = Items
        fields = ("name",)

class ManageLists(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ("name",)
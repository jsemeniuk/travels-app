from django import forms 
from .models import Items, Lists

class ManageItems(forms.ModelForm):
    item_done = forms.BooleanField(required=False)
    class Meta:
        model = Items
        fields = ("item_done", "name",)

class ManageLists(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Lists
        fields = ("name",)
# forms.py
from django import forms

class CreateItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.URLField()
    price = forms.DecimalField()
    available = forms.BooleanField(required=False)

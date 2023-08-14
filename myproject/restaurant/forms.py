from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Dish,Orders

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

class YourRegistrationForm(UserCreationForm):
    is_staff = forms.BooleanField(label='Are you a staff member?', required=False)

class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['delivery_address', 'contact_number']
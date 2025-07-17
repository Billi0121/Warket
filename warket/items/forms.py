from django.forms import ModelForm
from django import forms
from .models import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['item', 'price', 'description', 'image']
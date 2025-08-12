# from django.forms import ModelForm
from django import forms
from .models import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['item', 'price', 'description', 'image', 'Category']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['item', 'owner']

class ProductRateForm(forms.ModelForm):
    class Meta:
        model = ProductRate
        fields = ['rate', 'description',]
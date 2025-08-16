from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('item', 'price') 
        # ('item','description','owner', 'price', 'Category', 'currency', 'model', 'image')
from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.Serializer):
    class Meta:
        model = Products
        fields = ['item','description','owner', 'price', 'Category', 'currency', 'model', 'image']
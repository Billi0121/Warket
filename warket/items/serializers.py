from rest_framework import serializers

from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("item", "price")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("slug",)


class Group_type_groupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorylist
        fields = ("slug", "category_slug")

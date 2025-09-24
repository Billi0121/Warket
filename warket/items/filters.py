import django_filters

from .models import Products


class ProductsFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = ["item", "owner", "price"]

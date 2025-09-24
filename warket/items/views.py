from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .filters import ProductsFilter
from .forms import ProductsForm, CartForm, ProductRateForm, CategoryForm, Category2Form
from .models import Products, Category, Categorylist, Categorylist2, Cart, ProductRate

# Create your views here.


def home(requests):
    products = Products.objects.all()
    search = ProductsFilter()
    context = {
        "products": products,
        "search": search,
    }
    return render(requests, "items/index.html", context)


def adding_product(request):
    user = request.user
    form = ProductsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        Products = form.save(commit=False)
        Products.owner = request.user
        Products.currency = "$"
        category = form.cleaned_data["Category"]
        print(category)
        form.save()
        return redirect("home")
    context = {
        "form": form,
        "user": user,
    }
    return render(request, "items/adding_product.html", context)



def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    form = CartForm(request.POST or None)
    product_rate = ProductRate.objects.filter(product=pk)
    user = request.user
    product_rate_user = ProductRate.objects.filter(user=user).filter(product=pk)
    if form.is_valid():
        Productss = form.save(commit=False)
        Productss.item = product
        Productss.owner = request.user
        form.save()
        return redirect("home")
    context = {
        "form": form,
        "product": product,
        "product_rate": product_rate,
        "product_rate_user": product_rate_user,
    }
    return render(request, "items/product_detail.html", context)


def cart(request):
    user = User.objects.get(pk=request.user.id)
    users = Cart.objects.filter(owner=user)
    context = {
        "cart": users,
    }
    return render(request, "items/cart.html", context)


def cart_delete(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    return redirect("cart")


def product_delete(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()


def product_edit(request, pk):
    product = Products.objects.get(pk=pk)
    form = ProductsForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect("product_detail", product.id)
    return render(request, "items/adding_product.html", {"form": form})


def category(request):
    category = Category.objects.all()
    context = {
        "category": category,
    }
    return render(request, "items/category.html", context)


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    step2_category = category.category_slug.all()
    context = {"category": step2_category}
    return render(request, "items/category2.html", context)


def category2(request, slug, slug2):
    categ = Category.objects.get(slug=slug)
    categ2 = Categorylist.objects.get(slug=slug2)
    product = Products.objects.filter(Category=categ).filter(Category2=categ2)
    context = {"hello": "hello", "product": product}
    return render(request, "items/categories_product.html", context)


def product_rate_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    form = ProductRateForm(request.POST or None)
    if form.is_valid():
        Rate = form.save(commit=False)
        Rate.user = request.user
        Rate.product = product
        form.save()
    context = {
        "form": form,
    }
    return render(request, "items/product_rate.html", context)


def user_info(request, username):
    user = User.objects.get(pk=username)
    items = Products.objects.filter(owner=username)
    context = {"user": user, "items": items}
    return render(request, "items/user_information.html", context)


""" API VIEW """


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from .models import *
from .serializers import *


class ProductSerializerView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Group_type_groupView(viewsets.ModelViewSet):
    queryset = Categorylist.objects.all()
    serializer_class = Group_type_groupSerializer

from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def authorizade_only(func):
    def cheking_user(request, *args ,**kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect ('users:login')
    return cheking_user()

def home(request):
    items = Products.objects.all()
    return render(request, 'items/index.html', {'items': items})


def adding_product(request):
    user = request.user
    form = ProductsForm(
        request.POST or None,
        request.FILES or None)
    if form.is_valid():
        Products = form.save(commit=False)
        Products.owner = request.user
        Products.currency = '$'
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'items/adding_product.html', context)


def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    form = CartForm(request.POST or None)
    if form.is_valid():
        Productss = form.save(commit=False)
        Productss.item = product
        Productss.owner = request.user
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'items/product_detail.html', context)

def cart(request):
    user = User.objects.get(pk=request.user.id)
    users = Cart.objects.filter(owner=user)
    context = {
        'cart': users,

    }
    return render(request, 'items/cart.html', context)

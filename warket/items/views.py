from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

def authorizade_only(func):
    def cheking_user(request, *args ,**kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect ('users:login')
    return cheking_user()

def home(request):
    product = Products.objects.all()
    return render(request, 'items/index.html', {'product': product})


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

def cart_delete(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    return redirect('cart')

def product_delete(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect('home')

def product_edit(request, pk):
    product = Products.objects.get(pk=pk)
    form = ProductsForm(
        request.POST or None,
        instance=product
        )
    if form.is_valid():
        form.save()
        return redirect('product_detail', product.id)
    return render(request, 'items/adding_product.html', {'form': form})

def category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'items/category.html', context)

def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    product = Products.objects.filter(Category=category)
    context = {
        'product': product,
    }
    return render(request, 'items/index.html', context)
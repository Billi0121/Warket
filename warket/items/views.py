from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

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

from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request, 'items/index.html')


def adding_product(request):
    form = ProductsForm(
        request.POST or None,
        request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'items/adding_product.html', context)

from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def home(request):
    items = Products.objects.all()
    return render(request, 'items/index.html', {'items': items})


def adding_product(request):
    form = ProductsForm(
        request.POST or None,
        request.FILES or None)
    if form.is_valid():
        # form = Products.save(commit=False)
        item = form.cleaned_data['item']
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'items/adding_product.html', context)

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth import logout
# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

def logoutview(request):
    logout(request)
    return redirect('home')
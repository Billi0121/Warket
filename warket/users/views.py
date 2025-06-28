from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:login")


def logoutview(request):
    logout(request)
    return redirect("home")


def user(request, username):
    user = User.objects.get(username=request.user)
    context = {"user": user}
    return render(request, "users/userp.htlm", context)

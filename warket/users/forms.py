from django.contrib.auth.forms import *
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class SignUpForm(UserCreationForm):
    profile_photo = forms.CharField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name' ,'last_name', 'email', 'password1', 'password2', 'profile_photo']
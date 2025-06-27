from django.contrib.auth.forms import *
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'
from django.contrib.auth.forms import *
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name' ,'last_name', 'email', 'password1', 'password2']
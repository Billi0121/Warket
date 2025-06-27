from django.urls import path
from django.contrib.auth.views import LoginView
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html')),
    path('signuo/', views.SignUpView)
]
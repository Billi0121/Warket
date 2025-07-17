from django.urls import path
from django.contrib.auth.views import LoginView
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html') ,name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logoutview, name='logout')
]
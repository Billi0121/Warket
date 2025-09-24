"""
URL configuration for warket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from items import views
from items.views import *
from items.views import ProductSerializerView

routers = DefaultRouter()
routers.register(r"products", ProductSerializerView, basename="psv")
routers.register(r"category", CategoryView)
routers.register(r"category_group", Group_type_groupView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("api/", include(routers.urls)),
    path("", include("users.urls", namespace="auth")),
    path("adding_product/", views.adding_product, name="adding_product"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("cart/<int:pk>/", views.cart_delete, name="cart_delete"),
    path("product_delete/<int:pk>/", views.product_delete, name="product_delete"),
    path("product_edit/<int:pk>/", views.product_edit, name="product_edit"),
    path("category/", views.category, name="category"),
    path("category/<slug:slug>/", views.get_category, name="get_category"),
    path("category/<slug:slug>/<slug:slug2>/", views.category2, name="category2"),
    path("rate/<int:pk>/", views.product_rate_view, name="product_rate_view"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

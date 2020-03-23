"""shoestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api import views
from api.models import Shoe, ShoeColor, ShoeType, Manufacturer
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'shoe', views.ShoeViewSet)
router.register(r'shoecolor', views.ShoeColorViewSet)
router.register(r'shoetype', views.ShoeTypeViewSet)
router.register(r'manufacturer', views.ManufacturerViewSet)

admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Manufacturer)

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

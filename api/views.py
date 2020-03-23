from django.shortcuts import render
from api.models import Shoe, ShoeColor, ShoeType, Manufacturer
from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer, ShoeSerializer, \
    ShoeColorSerializer, ShoeTypeSerializer, ManufacturerSerializer
# Create your views here.
# Viewsets group together similar model behaviour and handle formatting
# of the serialized data into a HTTP-compatible response


def index(request):
    return render(request, 'index.html', {'news': "NewsItem.objects.all()"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

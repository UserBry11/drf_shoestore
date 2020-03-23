from django.contrib.auth.models import User
from api.models import ShoeType, ShoeColor, Shoe, Manufacturer
from rest_framework import serializers
# Serializers convert model objects into usable JSON format


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_name']


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']

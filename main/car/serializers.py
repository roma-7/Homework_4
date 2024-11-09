from .models import Marka, CarModel, Car
from rest_framework import serializers


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name','car_marka', 'car_model', 'description', 'year', 'millage', 'price', 'color', 'volume', 'have', 'image',
                  'video']

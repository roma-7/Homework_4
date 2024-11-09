from django_filters import FilterSet
from .models import *


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'car_name': ['exact'],
            'year': ['exact'],
            'price': ['gt', 'lt'],
        }

from django_filters.rest_framework import DjangoFilterBackend
from .models import CarModel, Car, Marka
from .filters import CarFilter
from .serializers import MarkaSerializer, CarModelSerializer,CarSerializer
from rest_framework import viewsets, permissions


class MarkaView(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer


class CarModelView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

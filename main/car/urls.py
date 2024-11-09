from django.urls import path
from .views import MarkaView, CarView, CarModelView

urlpatterns = [
    path('',CarView.as_view({'get': 'list', 'post':'create'}), name='product'),
    path('<int:pk>/', CarView.as_view({'get':'retrieve',
                                              'put':'update',
                                              'delete':'destroy'}), name='product-detail'),

    path('category/', CarView.as_view({'get': 'list', 'post': 'create'}), name='category'),

    path('category/<int:pk>/', CarView.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='category-detail'),
]
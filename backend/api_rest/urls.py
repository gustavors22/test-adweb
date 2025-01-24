from django.urls import path

from .views import ProductResourceAPIView, ProductDeleteAPIView

urlpatterns = [
    path('products', ProductResourceAPIView.as_view(), name='api_rest_products_get_post'),
    path('products/<uuid:id>', ProductDeleteAPIView.as_view(), name='api_rest_products_delete'),
]

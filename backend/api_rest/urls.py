from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductResourceAPIView, ProductDeleteAPIView

urlpatterns = [
    path('products', ProductResourceAPIView.as_view(), name='api_rest_products_get_post'),
    path('products/<uuid:id>', ProductDeleteAPIView.as_view(), name='api_rest_products_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

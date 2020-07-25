from django.urls import path, include
from fresh_produce_api import views
from rest_framework.routers import DefaultRouter

app_name = 'Masikane'

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product-viewset')

urlpatterns = [
    path('', include(router.urls)),
]
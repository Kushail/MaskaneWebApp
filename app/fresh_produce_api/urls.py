from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fresh_produce_api import views

router = DefaultRouter()
router.register('product-viewset', views.ProductViewset, basename='product-viewset')

app_name = 'Masikane'

urlpatterns = [
    path('', include(router.urls))
]
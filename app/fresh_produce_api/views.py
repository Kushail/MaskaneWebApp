from rest_framework import viewsets
from fresh_produce_api import serializers
from fresh_produce_api.models import Product


# Create your views here.
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    """Handle creating and getting of products"""
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

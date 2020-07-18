from django.shortcuts import render
from rest_framework import viewsets, mixins
from fresh_produce_api import serializers
from fresh_produce_api.models import Product


# Create your views here.
class ProductViewset(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Handle creating and getting of products"""
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        """Return all product objects"""
        return self.queryset()

    def perform_create(self, serializer):
        """Create product object"""
        serializer.save()
    
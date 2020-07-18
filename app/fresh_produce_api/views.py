from django.shortcuts import render
from rest_framework import viewsets
from fresh_produce_api import serializers, models

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
from rest_framework import serializers
from fresh_produce_api import models

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    grade = serializers.CharField(max_length=5)
    min_quantity = serializers.IntegerField()
    is_in_stock = serializers.BooleanField()

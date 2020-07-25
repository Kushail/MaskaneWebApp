from rest_framework import serializers
from fresh_produce_api import models

class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""
    
    class Meta:
        model = models.Product
        fields = '__all__'
    
    def create(self, validated_data):
        """Handle creating product"""
        product = models.Product.objects.create_product(
            name=validated_data['name'],
            price=validated_data['price'],
            grade=validated_data['grade'],
            min_quantity=validated_data['min_quantity'],
            is_in_stock=validated_data['is_in_stock'],
        )
        return product

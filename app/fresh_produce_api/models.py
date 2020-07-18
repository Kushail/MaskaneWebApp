from django.db import models

# Create your models here.
class Product(models.Model):
    """Model for products"""
    name = models.CharField(max_length=200)
    price = models.FloatField()
    grade = models.CharField(max_length=5)
    min_quantity = models.IntegerField()
    is_in_stock = models.BooleanField()

    def __str__(self):
        """Return string representation of product"""
        return self.name

    def get_full_name(self):
        """Return full name"""
        return self.name

    def get_short_name(self):
        """Return short name"""
        return self.name

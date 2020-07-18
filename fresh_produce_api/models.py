from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    grade = models.CharField(max_length = 5)
    min_quantity = models.IntField()
    is_in_stock = models.BooleanField()

from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    dtoc = models.DateTimeField(auto_now_add=True)
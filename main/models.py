from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

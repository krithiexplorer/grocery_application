from django.db import models

# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(max_length=100)
    price = models.PositiveIntegerField(max_length=100)
    category = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_pics')
    description = models.TextField()

class Wishlisted(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(max_length=100)
    price = models.PositiveIntegerField(max_length=100)
    category = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_pics')
    description = models.TextField()    

class Cart(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(max_length=100)
    price = models.PositiveIntegerField(max_length=100)
    category = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_pics')
    description = models.TextField()   

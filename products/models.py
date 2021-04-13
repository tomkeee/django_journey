from django.db import models

# Create your models here.
class Product(models.Model):
    title       =models.TextField(default='0')
    description =models.TextField(default='0')
    price       =models.TextField(default='0')
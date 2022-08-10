
from random import choices
from statistics import mode
from django.db import models

from accounts.views import customer


# Create your models here.
class Customer(models.Model):
   
    name = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=200,null=True)
    dateCreated = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
   
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name="tags")

    def __str__(self):
        return self.name
    
      # create a class for products tags

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','pending'),
        ('Out for delivery','Out for delivery'),
        ('delivered','delivered'),
        ('paid','paid'),
    )
    customer = models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL, blank=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True, choices=STATUS_CHOICES)

    












          
            
          





     



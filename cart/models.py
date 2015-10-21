from django.db import models

# Create your models here.
from ecommerce.models import *


class Cart(models.Model):
    user = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    delivered_date = models.DateTimeField(auto_now=True)
    #items = models.ManyToManyField('Item')
    #items = models.ManyToManyField('Item',null=True)

class Item(models.Model):
    cart = models.ForeignKey(Cart,default=0)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Brand)
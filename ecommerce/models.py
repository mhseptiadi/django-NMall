from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    #pr
    image = models.ImageField(default='')
    email = models.EmailField(default='')
    price = models.DecimalField(default=0,max_digits=19, decimal_places=10)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:

            self .slug = slugify(self.title)

        super(Product, self).save(*args,**kwargs)

    def __str__(self):
        return "%s > %s" % (self.brand.name,self.title)

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)

    def __str__(self):
        #return self.parent.name + ' - ' + self.name
        return self.name

class Cart(models.Model):
    pass

class CartItem(models.Model):
    pass
from os import name
from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name

    
class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    suncategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="Shop/images", default="")

    def __str__(self):
        return self.Product_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_Json = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=10, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
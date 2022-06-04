from distutils.command.upload import upload
import numbers
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField
from rest_framework.authtoken.models import Token
# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=123)
    text = models.TextField()
    img = models.ImageField(upload_to = 'Slider/')


class News(models.Model):
    name = models.CharField(max_length=123)
    text = models.TextField()
    img = models.ImageField(upload_to = 'News/')
    date = models.DateField()

class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    turi  = models.CharField(max_length=123)
    img = models.ImageField(upload_to = 'Product/')
    price = models.FloatField()
    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    email = models.EmailField()

class Info(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()

class ContactUs(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    number = models.IntegerField()
    adress = models.CharField(max_length=123)
    message = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    totle_price = models.IntegerField()

class OrderItem(models.Model):
    order  = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.account
        
class Shop(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name.encode('utf-8', errors='replace')
    
class Meal(models.Model):
    shop_id = models.ForeignKey('Shop')
    meal_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name.encode('utf-8', errors='replace')

class Order(models.Model):
    order_id = models.CharField(max_length=200, primary_key=True)
    user_id = models.ForeignKey('User')
    shop_id = models.ForeignKey('Shop')
    meals = models.CharField(max_length=200)
    total_price = models.CharField(max_length=200)
    order_time = models.DateTimeField(default=timezone.now)
    pickup_time = models.DateTimeField(default=timezone.now)
    
    def post(self):
        self.order_date = timezone.now()

    def __str__(self):
        return self.order_id
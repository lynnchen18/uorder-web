from django.contrib.auth.models import User, Group
from rest_framework import serializers
from dataaccess.models import Meal, Shop, Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('shop_id', 'meal_id', 'name', 'price', 'cover', 'info')
        
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('shop_id', 'name', 'cover')
        
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'user_id', 'shop_id', 'meals', 'total_price', 'order_time', 'pickup_time')
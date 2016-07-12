from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.core import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dataaccess.serializers import UserSerializer, GroupSerializer, MealSerializer, ShopSerializer, OrdersSerializer
from models import Meal, Shop
from rest_framework.renderers import JSONRenderer
from django.views.generic import ListView

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


import json



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

def meals_json(request):
    meals = Meal.objects.all()
    serializer = MealSerializer(meals,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)
    
def shops_json(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)
    
def shop_json(request, shop_num):
    shop_num = str(shop_num)
    if len(shop_num) < 2:
        shop_num = '0' + shop_num
    shop = Shop.objects.filter(shop_id = shop_num)
    serializer = ShopSerializer(shop,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)

def shop_meals_json(request, shop_num):
    meals = Meal.objects.filter(shop_id = shop_num)
    serializer = MealSerializer(meals,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)
    
def meal_json(request, meal_num):
    meal = Meal.objects.filter(meal_id = meal_num)
    serializer = MealSerializer(meal,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)
    
def records_json(request, user_num):
    orders = Order.objects.filter(user_id = user_num)
    serializer = OrdersSerializer(order,many=True)
    json = JSONRenderer().render(serializer.data)
    print json
    return HttpResponse(json)

# @api_view(['GET'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))

class SaveMealClass(ListView):
    def get(self, request):
        return HttpResponse("Hello")
      
    def post(self, request):
        json.loads(reguest.body)
        print request.post
        print request.body
        return HttpResponse("Done")

# class TestView(api.APIView):
#   queryset = BaseUser.objects.all()

#   def get_permissions(self):
#       if self.request.method == 'POST':
#           return (permissions.AllowAny(),)

#       return (permissions.IsAuthenticated(),)
        
# def print_meals(request):
    
#     serializer = MealSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
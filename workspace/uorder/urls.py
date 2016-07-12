from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from dataaccess import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^meals/', views.meals_json),
    url(r'^shops/', views.shops_json),
    url(r'^shop(?P<shop_num>\d+)/', views.shop_json),
    url(r'^shop(?P<shop_num>\d+)meals/', views.shop_meals_json),
    url(r'^meal(?P<meal_num>[0-9]{3})/', views.meal_json),
    url(r'^records(?P<user_num>\d+)/', views.records_json),
    # url(r'^print_meals/',views.SaveMealClass.as_view(), name='SaveMealClass'),
    url(r'^print_meals/',views.SaveMealClass.as_view()),
    # url(r'^test/', views.TestView.as_view, name='TestView'),
]
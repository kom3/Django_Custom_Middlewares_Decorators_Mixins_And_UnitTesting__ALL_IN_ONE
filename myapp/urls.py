from rest_framework.request import Request
from django.http import HttpRequest
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

myrouter = DefaultRouter()
myrouter.register('users', views.PostViewSet)


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.Home, name="home"),
    path("dcrfriend", views.decorator_friend),
    path("users", include(myrouter.urls)),
    path("gettoken", views.gettoken),
    path('managefreecustomers/', views.ManageFreeCustomers.as_view(),
         name="managefreecustomers"),
    path('managepremiumcustomers/', views.ManagePremiumCustomers.as_view(),
         name="managepremiumcustomers")

]


django_request = HttpRequest()
django_request.method = 'GET'

my_view = views.PostViewSet.as_view({'get': 'retrieve', 'post': 'create'})
data = my_view(request=django_request, pk=1)


print(f'data in URLs: {data.data}\n')

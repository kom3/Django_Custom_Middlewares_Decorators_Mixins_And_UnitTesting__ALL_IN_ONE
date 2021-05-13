from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

myrouter = DefaultRouter()
myrouter.register('users', views.PostViewSet)


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.Home),
    path("dcrfriend", views.decorator_friend),
    path("users", include(myrouter.urls)),
    path("gettoken", views.gettoken),
]


from django.http import HttpRequest
from rest_framework.request import Request

django_request = HttpRequest()
django_request.method = 'GET'

my_view = views.PostViewSet.as_view({'get': 'retrieve', 'post':'create'})
data = my_view(request=django_request, pk=1)


print(f'data in URLs: {data.data}\n')

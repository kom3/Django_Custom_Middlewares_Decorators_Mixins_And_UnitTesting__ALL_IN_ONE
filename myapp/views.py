from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .mycustomdecorators import mycustomdecorator, mycallablecustomdecorator
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUserModel, MyAnotherModel
from .serializers import MyUserSerializer, MyAnotherSerializer
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@csrf_exempt
@ensure_csrf_cookie
def Home(request):
    users = MyUserModel.objects.using('mysql').filter(age=23)
    print(bool(users))
    primitive__user_data = MyUserSerializer(users, many=True)

    print(primitive__user_data.data)
    voters = MyAnotherModel.objects.using('mysql').all()
    primitive__voter_data = MyAnotherSerializer(voters, many=True)
    print(primitive__voter_data.data)
    return render(request, 'registration/login.html')


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = MyUserModel.objects.using('mysql').all()
    serializer_class = MyUserSerializer


# @mycustomdecorator

@mycallablecustomdecorator("allow")
def decorator_friend(request):
    print("\ncontext:", request.extra_info, end='\n\n')
    return HttpResponse("Hi, I am decorators friend...", str(request.user))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   DRF Token authentication @@@@@@@@@@@@@@@@@@


# from rest_framework.request import Request
# from django.db.models import Q
# from django.db.models import F

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# from django.contrib.auth import login
from django.core.serializers import serialize


@login_required
def gettoken(request):
    # request = dict(request)
    token = Token.objects.filter(user=request.user)
    token = serialize('json', token)
    if not token:
        token = Token.objects.create(user=request.user)
        token = token.key
    print(token)
    response = {"status": 200, "message": token}
    return HttpResponse(json.dumps(response))

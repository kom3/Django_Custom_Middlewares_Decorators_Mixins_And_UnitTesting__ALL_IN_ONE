from .mycustommixins import MyCustGenListMixin
from django.views import View
from django.core.serializers import serialize
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
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

# from django.contrib.auth import login

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Existing super Users in db:
# admin:test
# user:test
# user1:test
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++


@login_required
def gettoken(request):
    # request = dict(request)
    token = Token.objects.filter(user=request.user)
    if not token:
        print("Token not found | Generating...")
        token = Token.objects.create(user=request.user)
        token = token.key
        print("Generated Token:", token)
    else:
        token = serialize('json', token)
        token = json.loads(token)
        print("Data form db:", token, type(token))
        token = token[0].get('pk')
        print("Token Found In DB:", token)

    response = {"status": 200, "message": token}
    return HttpResponse(json.dumps(response))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Custom Mixin in class view  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class ManagePremiumCustomers(MyCustGenListMixin, View):
    cust_data = {"customers": ["Iron man",
                               "Thanos", "Captain America", "Ant man"]}
    template = "premium_cust.html"


class ManageFreeCustomers(MyCustGenListMixin, View):
    cust_data = {"customers": ["Manju", "Anil", "Brian"]}
    template = "normal_cust.html"

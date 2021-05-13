from rest_framework import serializers
from .models import MyUserModel, MyAnotherModel
from rest_framework.authtoken.models import Token

class MyUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MyUserModel
        fields = "__all__"

class MyAnotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAnotherModel
        fields = '__all__'

from django.contrib import admin
from .models import MyAnotherModel, MyUserModel
from rest_framework.authtoken.models import Token
# Register your models here.



admin.site.register(MyUserModel)
admin.site.register(MyAnotherModel)
# admin.site.register(Token) #by default it will be registered to admin site
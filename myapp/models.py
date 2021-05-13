from django.db import models
# Create your models here.

class MyUserModel(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class MyAnotherModel(models.Model):
    # id = models.CharField(max_length=200)
    votingpower = models.BooleanField()
    voter = models.ForeignKey(MyUserModel, on_delete = models.CASCADE)
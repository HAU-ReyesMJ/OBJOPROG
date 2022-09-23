from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class Account(models.Model):
    lastName    =   models.CharField(max_length=120)

class User(AbstractBaseUser):
    balanceA = models.IntegerField()
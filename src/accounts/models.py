from turtle import title
from unicodedata import name
from django.db import models

class Account(models.Model):
    lastName    =   models.CharField(max_length=120)
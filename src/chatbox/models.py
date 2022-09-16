from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Chatbox(models.Model):
    recepient     = models.EmailField(max_length=120)
    messages      = models.TextField(max_length=1200)
    date          = models.DateField()
    messageType   = models.IntegerField()
    # title       = models.CharField(max_length=120)
    # description = models.TextField()
    # price       = models.DecimalField(decimal_places=2, max_digits=1000)
    # name        = models.TextField(null=True)
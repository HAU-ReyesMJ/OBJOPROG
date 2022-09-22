# from turtle import title
# from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class Contacts(models.Model):
    firstName   = models.TextField(null=True, blank=True)
    lastName    = models.TextField(null=True, blank=True)
    # price       = models.DecimalField(decimal_places=2, max_digits=1000)
    # name        = models.TextField(null=True, blank=True)
    # location    = models.TextField(null=True, blank=True)
    # markAsSold  = models.BooleanField()

    # def get_absolute_url(self):
    #     return reverse("item:item_edit", kwargs={"id": self.id})
    #     # return f"products/{self.id}/"

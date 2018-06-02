from django.db import models
from django.utils import timezone
from agent.models import Agent


# Create your models here.

class PropertyType(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Property(models.Model) :
    name = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, verbose_name='Agent')
    price = models.FloatField(verbose_name='Property Price')
    description = models.TextField(verbose_name='Property Details')
    location = models.CharField(max_length=200, verbose_name='Property Location')
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, verbose_name='Property Type')
    sale_type = models.CharField(max_length=100, verbose_name='Type of Sale')
    date_added = models.DateField(default=timezone.now, verbose_name='Date Registered')
    bedrooms = models.IntegerField(default=0, verbose_name='Number of Bedrooms')
    kitchens = models.IntegerField(default=0, verbose_name='Number of Kitchens')
    living_rooms = models.IntegerField(default=0, verbose_name='Number of Living Rooms')
    parking = models.IntegerField(default=0, verbose_name='Number of Parking Lots')
    picture_1 = models.ImageField(upload_to='property/%s'%(timezone.now()))
    picture_2 = models.ImageField(blank=True, null=True, upload_to='property/%s'%(timezone.now()))
    picture_3 = models.ImageField(blank=True, null=True, upload_to='property/%s'%(timezone.now()))
    picture_4 = models.ImageField(blank=True, null=True, upload_to='property/%s'%(timezone.now()))

    class Meta :
        verbose_name_plural = 'Properties'


    def __str__(self):
        return self.name
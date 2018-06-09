from django.contrib import admin
from .models import Property, SaleType, BuildingType


# Register your models here.
admin.site.register(Property)
admin.site.register(SaleType)
admin.site.register(BuildingType)
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .models import Property, PropertyType
from .forms import PropertyForm, PropertyTypeForm
from .models import Property
from django.urls import reverse_lazy


# Create your views here.
class PropertyCreateView(CreateView) :
    template_name_suffix = '_create_form'
    model = Property
    fields = ('price', 'description', 'location', 'property_type', 'sale_type', 'bedrooms', 'kitchens', 'living_rooms', 'parking', \
              'picture_1', 'picture_2', 'picture_3', 'picture_4')
    success_url = reverse_lazy('property:success_create')


class PropertyUpdateView(UpdateView) :
    template_name_suffix = '_update_form'
    model = Property
    fields = ('price', 'description', 'location', 'property_type', 'sale_type', 'bedrooms', 'kitchens', 'living_rooms', 'parking', \
              'picture_1', 'picture_2', 'picture_3', 'picture_4')
    success_url = reverse_lazy('property:success_update')


class PropertyListView(ListView) :
    paginate_by = 10
    queryset = Property.objects.all()
    model = Property


def success_create(request) :
    return render(request, 'property/success_create.html')


def success_update(request) :
    return render(request, 'property/success_update.html')
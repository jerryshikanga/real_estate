from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property, PropertyEnquiry
from django.urls import reverse_lazy


# Create your views here.
def hot_properties(number):
    property_list = Property.objects.filter(availability=True)[:number]
    return property_list


class PropertyCreateView(LoginRequiredMixin, CreateView):
    template_name_suffix = '_create_form'
    model = Property
    fields = (
    'price', 'description', 'location', 'property_type', 'sale_type', 'bedrooms', 'kitchens', 'living_rooms', 'parking', \
    'picture_1', 'picture_2', 'picture_3', 'picture_4')
    success_url = reverse_lazy('property:success_create')


class PropertyDeleteView(DeleteView):
    model = Property


class PropertyUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    model = Property
    fields = (
    'price', 'description', 'location', 'property_type', 'sale_type', 'bedrooms', 'kitchens', 'living_rooms', 'parking', \
    'picture_1', 'picture_2', 'picture_3', 'picture_4')
    success_url = reverse_lazy('property:success_update')


class PropertyDetailView(DetailView):
    model = Property
    extra_context = {
        'hot_property_list': hot_properties(4)
    }


class PropertyListView(ListView):
    paginate_by = 10
    extra_context = {
        'hot_property_list': hot_properties(4)
    }

    def get_queryset(self):
        name = self.request.GET.get("name")
        property_type = self.request.GET.get("property_type")
        min_price = self.request.GET.get("min")
        max_price = self.request.GET.get("max")

        property_list = Property.objects.all()

        if name is not None:
            property_list = property_list.filter(name__icontains=name)
        if property_type is not None:
            property_list = property_list.filter(property_type=property_type)
        if min_price is not None and min_price is not "":
            property_list = property_list.filter(price__gte=float(min_price))
        if max_price is not None and max_price is not "":
            property_list = property_list.filter(price__lte=float(max_price))
        return property_list

    model = Property


class NewEnquiryView(CreateView):
    model = PropertyEnquiry
    fields = ('property', 'name', 'email', 'telephone', 'message')
    success_url = reverse_lazy('property:success_query')


def success_create(request):
    return render(request, 'property/success_create.html')


def success_update(request):
    return render(request, 'property/success_update.html')


def success_inquiry(request):
    return render(request, 'property/success_inquiry.html')


def success_delete(request):
    return render(request, 'property/success_delete.html')

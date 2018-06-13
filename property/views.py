from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property, PropertyEnquiry
from django.urls import reverse_lazy
from agent.models import Agent
from django.shortcuts import redirect
from .forms import EnquiryForm


# Create your views here.
def hot_properties(number):
    property_list = Property.objects.filter(availability=True)[:number]
    return property_list


class PropertyCreateView(LoginRequiredMixin, CreateView):
    template_name_suffix = '_create_form'
    model = Property
    fields = (
        'name', 'price', 'location', 'description', 'building_type', 'sale_type', 'bedrooms', 'kitchens',
        'living_rooms', 'parking', \
        'picture_1', 'picture_2', 'picture_3', 'picture_4')

    def form_valid(self, form):
        agent = Agent.objects.get(user=self.request.user)
        self.object = form.save()
        self.object.agent = agent
        self.object.save()
        return redirect(reverse_lazy("property:detail", kwargs={'pk':self.object.id}))


class PropertyDeleteView(DeleteView):
    model = Property


class PropertyUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    model = Property
    fields = (
        'name', 'price', 'description', 'location', 'building_type', 'sale_type', 'bedrooms', 'kitchens',
        'living_rooms', 'parking', \
        'picture_1', 'picture_2', 'picture_3', 'picture_4')
    # success_url = reverse_lazy('property:success_update')


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
        building_type = self.request.GET.get("building_type")
        sale_type = self.request.GET.get("sale_type")
        min_price = self.request.GET.get("min")
        max_price = self.request.GET.get("max")

        property_list = Property.objects.all()

        if name is not None:
            property_list = property_list.filter(name__icontains=name)
        if sale_type is not None :
            property_list = property_list.filter(sale_type=sale_type)
        if building_type is not None:
            property_list = property_list.filter(building_type=building_type)
        if min_price is not None and min_price is not "":
            property_list = property_list.filter(price__gte=float(min_price))
        if max_price is not None and max_price is not "":
            property_list = property_list.filter(price__lte=float(max_price))
        return property_list

    model = Property


class NewEnquiryView(LoginRequiredMixin, FormView):
    form_class = EnquiryForm
    template_name = 'property/propertyenquiry_form.html'

    def get_success_url(self):
        return reverse_lazy('property:detail', kwargs={'pk':self.kwargs['property_id']})

    def form_valid(self, form):
        property = Property.objects.get(pk=self.kwargs['property_id'])
        form.save_inquiry(self.request.user, property=property)
        return super(NewEnquiryView, self).form_valid(form)


class InquiryDetail(DetailView) :
    model = PropertyEnquiry

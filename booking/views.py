from django.views.generic import FormView, ListView
from .forms import BookingForm, SelectedBookingForm
from .models import Booking
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from property.models import Property


# Create your views here.
class NewBooking(LoginRequiredMixin, FormView) :
    form_class = BookingForm
    success_url = reverse_lazy('booking:success_new')
    template_name = 'booking/booking_form.html'

    def form_valid(self, form):
        form.save_booking(self.request.user)
        return super(NewBooking, self).form_valid(form)


class SelectedBookingView(LoginRequiredMixin, FormView) :
    form_class = SelectedBookingForm
    success_url = reverse_lazy('booking:success_new')
    template_name = 'booking/booking_form.html'

    def form_valid(self, form):
        m_property = Property.objects.get(pk=self.kwargs['property_id'])
        form.save_selected_booking(m_property=m_property, user=self.request.user)
        return super(SelectedBookingView, self).form_valid(form)


class BookingList(ListView) :
    paginate_by = 10
    queryset = Booking.objects.all()


def success_booking(request, *args, **kwargs) :
    return render(request, 'booking/success_booking.html')
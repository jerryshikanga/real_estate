from django import forms
from django.utils import timezone
from property.models import Property
from .models import Booking
from datetime import datetime


class BookingForm(forms.Form) :
    property = forms.ModelChoiceField(queryset=Property.objects.all(), required=True)
    date_start = forms.DateField(required=True, widget=forms.DateInput,)
    date_end = forms.DateField(required=True, widget=forms.DateInput)

    def save_booking(self, user):
        booking = Booking.objects.create(
            property=self.cleaned_data['property'],
            date_starting=self.cleaned_data['date_start'],
            date_ending=self.cleaned_data['date_end'],
            user=user,
        )
        booking.save()


class SelectedBookingForm(forms.Form) :
    date_start = forms.DateField(required=True, widget=forms.SelectDateWidget ,)
    date_end = forms.DateField(required=True, widget=forms.SelectDateWidget, )

    def save_selected_booking(self, m_property, user):
        booking = Booking.objects.create(
            property=m_property,
            date_starting=self.cleaned_data['date_start'],
            date_ending=self.cleaned_data['date_end'],
            user=user,
        )
        booking.save()

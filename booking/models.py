from django.db import models
from property.models import Property
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Booking(models.Model) :
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name="Property Details")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User Booking")
    time_booking = models.DateTimeField(default=timezone.now, verbose_name="Date of booking")
    date_starting = models.DateField(verbose_name="Date of start of tenancy")
    date_ending = models.DateField(null=True, verbose_name="Date of end of tenancy")
    payment_status = models.BooleanField(default=False, verbose_name="Is payment made")

    class Meta:
        ordering = ('time_booking', 'date_starting', 'property')

    def __str__(self):
        return "Booking by %s on %s for %s" % (self.user.get_full_name(), self.time_booking, self.property.name)
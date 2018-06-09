from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path('new.html', views.NewBooking.as_view(), name='booking_new'),
    path('new/<int:property_id>/', views.SelectedBookingView.as_view(), name='booking_selected'),
    path('new/success.html', views.success_booking, name='success_new'),
    path('list.html/', views.BookingList.as_view(), name="list"),
]
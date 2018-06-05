from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('list.html', views.PropertyListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.PropertyDetailView.as_view(), name='detail'),
    path('new/', views.PropertyCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PropertyUpdateView.as_view(), name='update'),
    path('create/success.html', views.success_create, name='success_create'),
    path('update/success.html', views.success_update, name='success_update'),

    path('delete/<int:pk>', views.PropertyDeleteView.as_view(), name='delete'),
    path('delete/success.html', views.success_delete, name='success_delete'),

    # inquiries
    path('query/new/', views.NewEnquiryView.as_view(), name='enquiry_new'),
    path('query/success.html', views.success_inquiry, name='success_query'),
]
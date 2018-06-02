from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('list.html', views.PropertyListView.as_view(), name='list'),
    path('new/', views.PropertyCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PropertyUpdateView.as_view(), name='update'),
    path('create/success.html', views.success_create, name='success_create'),
    path('update/success.html', views.success_update, name='success_update'),
]
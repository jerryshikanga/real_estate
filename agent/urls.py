from django.urls import path
from . import views

app_name = "agent"

urlpatterns = [
    path('list.html', views.AgentListView.as_view(), name='list'),
    path('detail/<int:pk>', views.AgentDetailView.as_view(), name='detail'),
    path('register.html', views.AgentCreateView.as_view(), name='create'),
    path('create/success.html', views.success_agent_create, name='success_create'),
]
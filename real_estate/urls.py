"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', views.index, name='index_page'),
    path('', views.index, name='index_page'),
    path('about.html', views.about, name='about_page'),
    path('contact.html', views.contact, name='contact_page'),
    path('blog.html', views.blog, name='blog_page'),

    path('property/', include('property.urls')),
    path('agent/', include('agent.urls')),

    # for auth views
    path('auth/', include('django.contrib.auth.urls')),
]

# for serving media documents
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
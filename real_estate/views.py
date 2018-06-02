from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'index.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')

def contact(request, *args, **kwargs) :
    return  render(request, 'contact.html')

def blog(request, *args, **kwargs) :
    return render(request, 'blog.html')
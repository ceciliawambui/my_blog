from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def helloWorld(request):
    return HttpResponse('Hello, world!')

# def index(request):
#     return render(request, 'index.html')

def index(request):
    context = {'message': 'Hello, world!'}
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import BlogForm


from .models import Blog
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber


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


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogForm()
    
    return render(request, 'create_blog.html', {'form': form})
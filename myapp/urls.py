from django.urls import path 
from . import views 

urlpatterns = [ 
    # path('', views.helloWorld, name='hello'),
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/create/', views.create_blog, name='create_blog'),

]

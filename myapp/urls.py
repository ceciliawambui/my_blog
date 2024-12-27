from django.urls import path 
from . import views 


urlpatterns = [ 
    # path('', views.helloWorld, name='hello'),
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),


]
# add this for static files on deployment

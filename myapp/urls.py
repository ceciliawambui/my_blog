from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    # path('', views.helloWorld, name='hello'),
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_create/', views.blog_create, name='blog_create'),
    path('blog_edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('blog_delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('register/', views.user_registration, name='register'),
] 

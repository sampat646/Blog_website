from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('bloghome/', views.blog_home, name='blog_home'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
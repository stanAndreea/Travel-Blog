from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('discover',views.discover, name='discover'),
    path('discover/<slug:destination>/', views.discover_detail, name='discover_detail'),
    path('blog', views.blog, name='blog'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
]

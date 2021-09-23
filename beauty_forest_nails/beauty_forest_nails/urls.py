from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', include('services.urls')),
    path('rules/', views.rules, name='rules'),
    path('reviews/', include('reviews.urls')),
    path('about/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]

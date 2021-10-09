from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', include('services.urls')),
    path('reviews/', include('reviews.urls')),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('auth/', include('auth_reg.urls')),
    path('admin/', admin.site.urls),
]

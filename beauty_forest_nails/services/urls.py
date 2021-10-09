from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<str:service_type>', views.services, name='services-dynamic'),
]

from django.urls import path
from . import views

print("✅ Загрузка core/urls.py...")

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('appointment/', views.appointment, name='appointment'),
]

print("✅ Маршруты core загружены!")
